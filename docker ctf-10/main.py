from flask import Flask, request
import resource
from contextlib import redirect_stdout
import io, ast
import multiprocessing
import traceback

app = Flask(__name__)

@app.route("/")
def hello_world():
    body:str = request.json.get('body')
    stdout = io.StringIO()
    oldsoft, oldhard = resource.getrlimit(resource.RLIMIT_AS)
    limit_ram = 500 * 1024 * 1024 
    try:
        resource.setrlimit(resource.RLIMIT_AS, (limit_ram, oldhard))
        with redirect_stdout(stdout):
            def multiline_eval(expr, ctx={}):
                results = []
                for node in ast.parse(expr).body:
                    if isinstance(node, ast.Expr):
                        result = eval(compile(ast.Expression(node.value), '<string>', 'eval'), ctx)
                        results.append(result)
                    else:
                        module = ast.Module([node], type_ignores=[])
                        results.append(exec(compile(module, '<string>', 'exec'), ctx))
                print('\n'.join(map("str", results)))
            out = multiprocessing.Process(target=multiline_eval, args=(body,))
            out.start()
            out.join(timeout=30)
            if out.is_alive():
                out.kill()
                out.terminate()
                out.join()
                raise TimeoutError()
            ret = None
    except TimeoutError:
        outs = 'Python got TimeoutError'
    except MemoryError:
        outs = 'Python got MemoryError'
    except Exception:
        value = stdout.getvalue()
        outs = f'{value}{traceback.format_exc()}'
    else:
        value = stdout.getvalue()
        if ret is None:
            outs = f'{value}'
        else:
            outs = f'{value}{ret}'
    resource.setrlimit(resource.RLIMIT_AS, (oldsoft, oldhard))
    return {"out": outs}

app.run(port=1113, host="0.0.0.0")