from flask import Flask, redirect, url_for, abort, render_template
from markupsafe import escape

DEFAULT_GREETING_COUNT = 10
MAX_GREETING_COUNT = 100
REALLY_TOO_MANY_COUNT = 1000

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, world!"


@app.route("/hello/<string:username>/")
@app.route("/hello/<string:username>/<int:num>")
def personal_greetings(username, num=DEFAULT_GREETING_COUNT):
    if num >= REALLY_TOO_MANY_COUNT:
        abort(404)
    if num > MAX_GREETING_COUNT:
        return redirect(
            url_for("personal_greetings", username=username, num=DEFAULT_GREETING_COUNT)
        )
    greetings = ["Hello, " + escape(username) + "!"] * num
    return "<br/>".join(greetings)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page_not_found.html"), 404
