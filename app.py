from flask import Flask
import data
from anime import r_anime

app = Flask(__name__)
app.register_blueprint(r_anime, url_prefix='/anime')
li_data = []


@app.before_first_request
def init_datasets():
    li = data.preprocess_csv('Anime_data.csv')
    for row in li:
        li_data.append(row)


@app.before_first_request
def init_database():
    data.parse_genre(li_data)
    data.parse_producer(li_data)
    data.parse_source(li_data)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
