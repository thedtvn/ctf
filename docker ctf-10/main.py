from flask import Flask, request
import resource
from contextlib import redirect_stdout
import io, ast, uuid
import multiprocessing
import traceback

app = Flask(__name__)

manager = multiprocessing.Manager()
return_dict = manager.dict()

def multiline_eval(expr, pids, return_dict, ctx={}):
    stdout = io.StringIO()
    oldsoft, oldhard = resource.getrlimit(resource.RLIMIT_AS)
    limit_ram = 2 * 1024 * 1024 
    resource.setrlimit(resource.RLIMIT_AS, (limit_ram, oldhard))
    results = []
    try:
        with redirect_stdout(stdout):
            for node in ast.parse(expr).body:
                    if isinstance(node, ast.Expr):
                        outs = eval(compile(ast.Expression(node.value), '<string>', 'eval'), ctx)
                        results.append(outs)
                    else:
                        module = ast.Module([node], type_ignores=[])
                        results.append(exec(compile(module, '<string>', 'exec'), ctx))
            outsp = '\n'.join(map(str, [i for i in results if i is not None and i]))
    except Exception:
        outsp = f'{stdout.getvalue()}{traceback.format_exc()}'    
    resource.setrlimit(resource.RLIMIT_AS, (oldsoft, oldhard))
    return_dict[pids] = {"outsp": outsp, "stdout": stdout.getvalue()}
        
@app.route("/")
def hello_world():
    body:str = request.json.get('body')
    ret = ""
    stdout = ""
    pids = uuid.uuid4().hex
    try:
        out = multiprocessing.Process(target=multiline_eval, args=(body, pids, return_dict))
        out.start()
        out.join(timeout=30)
        if out.is_alive():
            out.kill()
            out.terminate()
            out.join()
            raise TimeoutError()
    except TimeoutError:
        outs = 'TimeoutError: Python got TimeoutError'
    except Exception:
        outs = f'{stdout}{traceback.format_exc()}'
    else:
        outspr = return_dict.get(pids, {})
        print(outspr)
        ret = outspr.get("outsp")
        stdout = outspr.get("stdout", "")
        try:
            del return_dict[pids]
        except KeyError:
            pass
        if not ret:
            outs = f'{stdout}'
        else:
            outs = f'{stdout}{ret}'
    return {"out": outs}

app.run(port=1113, host="0.0.0.0")