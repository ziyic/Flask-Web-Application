from flask import Flask
from anime import r_anime


app = Flask(__name__)
app.register_blueprint(r_anime, url_prefix='/anime')


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
