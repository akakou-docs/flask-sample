from flask import Flask
app = Flask(__name__)

html = """
<h1>ここはタイトル</h1>
<p>ここは文字</p>
<button>ここはボタン</button>
"""

@app.route("/hello")
def index():
    # /hello にアクセスした
    # ときここが呼ばれる
    return html

if __name__ == "__main__":
    # サーバ立ち上げ
    app.run(
        host="0.0.0.0",
        port=5002)
