from anime import anime
from flask import Flask, render_template
import data

app = Flask(__name__)
app.register_blueprint(anime)
li_data = []


@app.route('/')
def index():
    return render_template("index.html", title=hello_world())


def hello_world():
    return 'Anime Rating Gallery'


if __name__ == '__main__':
    app.run()
