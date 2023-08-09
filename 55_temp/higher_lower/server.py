import math
import random

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    return '<h1>Guess a number between 1 to 10</h1> <br><iframe src="https://giphy.com/embed/SQoYBYjcLUf2R3VM1u" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/wearethedoe-doe-the-thedoe-SQoYBYjcLUf2R3VM1u">via GIPHY</a></p>'


number = random.randint(1, 10)


@app.route("/user/<int:num>")
def num1(num):
    if abs(number - num) == 0:
        return '<h1>Found me !!</h1><iframe src="https://giphy.com/embed/uuQwZmRuX5G2d2u6cl" width="480" height="460" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/love-you-are-a-treasure-priceless-uuQwZmRuX5G2d2u6cl">via GIPHY</a></p>'
    elif number < num:
        return '<h2>Too high</h2><iframe src="https://giphy.com/embed/vU43V3ZzQC9xOibmxg" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/hackernoon-hacker-noon-dog-with-jetpack-vU43V3ZzQC9xOibmxg">via GIPHY</a></p>'
    else:
        return '<h2>Too low</h2><iframe src="https://giphy.com/embed/12bpEjD05ac2IM" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/loop-dig-12bpEjD05ac2IM">via GIPHY</a></p>'


if __name__ == '__main__':
    app.run(debug=True)
