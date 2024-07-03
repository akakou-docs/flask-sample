from flask import Flask, request
app = Flask(__name__)

template = """
<h1>Hello, {}!</h1>
"""

@app.route("/hello")
def index():
    name = request.args.get("name", default='Taro')
    return template.format(name)

if __name__ == "__main__":
    # サーバ立ち上げ
    app.run(
        host="0.0.0.0",
        port=5003)
