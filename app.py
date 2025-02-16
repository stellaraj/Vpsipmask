from flask import Flask, request, Response
import requests

app = Flask(__name__)

# Replace with your VPS IP and port
VPS_URL = "http://46.101.57.139:3000"

@app.route("/", defaults={"path": ""})
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    """Forward all requests to the VPS"""
    url = f"{VPS_URL}/{path}"
    
    if request.method == "GET":
        resp = requests.get(url, headers=request.headers)
    elif request.method == "POST":
        resp = requests.post(url, headers=request.headers, data=request.data)
    elif request.method == "PUT":
        resp = requests.put(url, headers=request.headers, data=request.data)
    elif request.method == "DELETE":
        resp = requests.delete(url, headers=request.headers)
    
    return Response(resp.content, status=resp.status_code, headers=dict(resp.headers))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
