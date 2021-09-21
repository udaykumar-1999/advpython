from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1> Hello World </h1>'


@app.route("/user/<name>")
def user(name):
    return f'<h1> Hello {name} </h1>'


@app.route("/headers")
def headers():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Your Browser is {user_agent}</p>'


if __name__ == '__main__':
    app.run(debug=True)
