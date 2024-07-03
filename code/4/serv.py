from flask import Flask, request
app = Flask(__name__)

template = """
<p>Hello, {}!</p>
<form action='/hello' method='post'>
  <input name='name'></input>
  <input type='submit'></input>
</form>
"""

@app.route("/hello", methods=['POST'])
def index():
    name = request.form["name"]
    return template.format(name)

if __name__ == "__main__":
    # サーバ立ち上げ
    app.run(
        host="0.0.0.0",
        port=5004)