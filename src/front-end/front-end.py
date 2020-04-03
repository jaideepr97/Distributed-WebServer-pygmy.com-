from flask import Flask
import requests

app = Flask(__name__)


@app.route('/search/<args>', methods=["GET"])
def search(args):
    query_url = 'http://127.0.0.1:5050/query_by_subject/' + str(args)
    query_result = requests.get(url=query_url)
    return query_result.json()


@app.route('/lookup/<args>', methods=["GET"])
def lookup(args):
    query_url = 'http://127.0.0.1:5050/query_by_item/' + str(args)
    query_result = requests.get(url=query_url)
    return query_result.json()


@app.route('/buy/<args>', methods=["GET"])
def buy(args):
    query_url = 'http://127.0.0.1:5051/buy/' + str(args)
    query_result = requests.get(url=query_url)
    return query_result.json()


if __name__ == '__main__':
    app.run(port=5052, debug=True)
