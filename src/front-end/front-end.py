from flask import Flask
import requests
import datetime
from flask import request
from IPython import embed
import threading

app = Flask(__name__)
edLab_url = 'http://elnux3.cs.umass.edu:34602'
edLab_order_url = 'http://elnux3.cs.umass.edu:34601'
local_url = 'http://0.0.0.0:34602'
local_order_url = 'http://0.0.0.0:34601'
log_lock = threading.Lock()


@app.route('/search/<args>', methods=["GET"])
def search(args):

    request_start = datetime.datetime.now()
    request_id = request.values['request_id']

    # query_url = local_url + '/query_by_subject/' + str(args)
    query_url = edLab_url + '/query_by_subject/' + str(args)

    query_result = requests.get(url=query_url, data={'request_id': request_id})

    request_end = datetime.datetime.now()
    request_time = request_end - request_start

    log_lock.acquire()
    file = open("front_end_server.txt", "a+")
    file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
    file.close()
    log_lock.release()

    return query_result.json()


@app.route('/lookup/<args>', methods=["GET"])
def lookup(args):

    request_start = datetime.datetime.now()
    request_id = request.values['request_id']

    # query_url = local_url + '/query_by_item/' + str(args)
    query_url = edLab_url + '/query_by_item/' + str(args)

    query_result = requests.get(url=query_url, data={'request_id': request_id})

    request_end = datetime.datetime.now()
    request_time = request_end - request_start

    log_lock.acquire()
    file = open("front_end_server.txt", "a+")
    file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
    file.close()
    log_lock.release()

    return query_result.json()


@app.route('/buy/<args>', methods=["GET"])
def buy(args):

    request_start = datetime.datetime.now()
    request_id = request.values['request_id']

    # query_url = local_order_url + '/buy/' + str(args)
    query_url = edLab_order_url + '/buy/' + str(args)

    query_result = requests.get(url=query_url, data={'request_id': request_id})

    request_end = datetime.datetime.now()
    request_time = request_end - request_start

    log_lock.acquire()
    file = open("front_end_server.txt", "a+")
    file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
    file.close()
    log_lock.release()

    return query_result.json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34600, debug=True)
