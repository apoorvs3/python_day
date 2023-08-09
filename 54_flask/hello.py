from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


def make_bold(arg):
    def wrapper_function():
        return f"<b>{arg()}</b>"

    return wrapper_function


def make_emphasis(args):
    def wrapper_function():
        return f"<em>{args()}</em>"

    return wrapper_function


def make_underlined(args):
    def wrapper_function():
        return f"<u>{args()}</u>"

    return wrapper_function


@app.route("/bye")
@make_bold
@make_underlined
@make_emphasis
def bye():
    return "<p>Bye</p>"


@app.route("/username/<path:name>")
def greet(name):
    return f"<h1 style='text-align : center'>hello there :  {name}</h1>" \
           f"<p>this is a para</p>" \
           f'<iframe src="https://giphy.com/embed/RW4Vf0698oX3W" width="480" height="323" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/kiss-new-girl-nick-RW4Vf0698oX3W">via GIPHY</a></p>'


@app.route("/user/<name>/<int:number>")
def greets(name, number):
    return f"hello there :  {name}, you are {number} years old"


if __name__ == '__main__':
    app.run(debug=True)
