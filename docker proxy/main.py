from flask import Flask, Response, request
import requests
import ipaddress

app = Flask(__name__)

def multiline_eval(expr, ctx={}):
    results = []
    for node in ast.parse(expr).body:
        if isinstance(node, ast.Expr):
            result = eval(compile(ast.Expression(node.value), '<string>', 'eval'), ctx)
            results.append(result)
        else:
            module = ast.Module([node], type_ignores=[])
            results.append(exec(compile(module, '<string>', 'exec'), ctx))
    return '\n'.join(map("str", results))

@app.route("/game-10/")
def hello_world():
    r = requests.get("http://10.5.0.2:1113", json=request.json)
    return Response(response=r.content, status=r.status_code)

@app.before_request
def block_requests():
    if ipaddress.ip_address(request.remote_addr) in ipaddress.ip_network('10.5.0.0/16'):
        return ":\\", 403


app.run(port=1112, host="0.0.0.0")