from flask import Flask
import requests

app = Flask(__name__)


@app.route('/search/<args>', methods=["GET"])
def search(args):
    query_url = 'http://elnux1.cs.umass.edu:34602/query_by_subject/' + str(args)
    query_result = requests.get(url=query_url)
    return query_result.json()


@app.route('/lookup/<args>', methods=["GET"])
def lookup(args):
    query_url = 'http://elnux1.cs.umass.edu:34602/query_by_item/' + str(args)
    query_result = requests.get(url=query_url)
    return query_result.json()


@app.route('/buy/<args>', methods=["GET"])
def buy(args):
    query_url = 'http://elnux2.cs.umass.edu:34601/buy/' + str(args)
    query_result = requests.get(url=query_url)
    return query_result.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34600, debug=True)
