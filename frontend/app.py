import os

from flask import Flask, render_template

_BASE = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(_BASE, "templates"),
    static_folder=os.path.join(_BASE, "static"),
    static_url_path="/static",
)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
