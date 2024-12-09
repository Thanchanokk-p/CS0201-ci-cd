from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, New World!</p>"


@app.route("/test")
def test():
    return "<p>Test Flask Server</p>"


@app.route("/info")
def info():
    import os
    return os.uname()


if __name__ == '__main__':
    app.run(debug=True)
