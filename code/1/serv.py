from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def index():
    # /hello にアクセスした
    # ときここが呼ばれる
    return "Hello World!"

if __name__ == "__main__":
    # サーバ立ち上げ
    app.run(
        host="0.0.0.0",
        port=5001)

