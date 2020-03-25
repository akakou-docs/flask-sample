from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/hello", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form["name"]
    else:
        name = "Taro"
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    # サーバ立ち上げ
    app.run(
        host="0.0.0.0",
        port=5005)
