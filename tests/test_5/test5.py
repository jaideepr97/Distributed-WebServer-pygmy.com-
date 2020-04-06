import uuid
import datetime
import requests
import random
import threading


def client_1():
    operations = ['search', 'lookup', 'buy']
    topics = ['distributed%20systems', 'graduate%20school']
    items = [1, 2, 3, 4]
    edLab_url = 'http://elnux3.cs.umass.edu:34602/'
    local_url = 'http://0.0.0.0:34600/'

    total_request_time = 0
    request_counter = 0

    for i in range(0, 50):
        request_id = uuid.uuid1()
        request_start = datetime.datetime.now()

        operation = random.choice(operations)
        if operation == 'search':
            topic = random.choice(topics)
            # query_url = edLab_url + '/' + str(operation) + '/' + str(topic)
            query_url = local_url + '/' + str(operation) + '/' + str(topic)
            request_result = requests.get(url=query_url, data={'request_id': request_id})
            file = open("client_1_output.txt", "a+")
            file.write(request_result.text)
            file.close()
            request_end = datetime.datetime.now()
            request_time = request_end - request_start
            total_request_time = total_request_time + (request_time.microseconds / 1000)
            request_counter = request_counter + 1
            file = open("client_1_metrics.txt", "a+")
            file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
            file.close()

        elif operation == 'lookup' or 'buy':
            item = random.choice(items)
            # query_url = edLab_url + '/' + str(operation) + '/' + str(item)
            query_url = local_url + '/' + str(operation) + '/' + str(item)
            request_result = requests.get(url=query_url, data={'request_id': request_id})
            file = open("client_1_output.txt", "a+")
            file.write(request_result.text)
            file.close()
            request_end = datetime.datetime.now()
            request_time = request_end - request_start
            total_request_time = total_request_time + (request_time.microseconds / 1000)
            request_counter = request_counter + 1
            file = open("client_1_metrics.txt", "a+")
            file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
            file.close()

    file = open("client_1_metrics.txt", "a+")
    file.write("Average request processing time: {}\n".format(total_request_time / request_counter))
    file.write("End to end request processing time: {}\n".format(total_request_time))
    file.close()


def client_2():
    operations = ['search', 'lookup', 'buy']
    topics = ['distributed%20systems', 'graduate%20school']
    items = [1, 2, 3, 4]
    edLab_url = 'http://elnux3.cs.umass.edu:34602/'
    local_url = 'http://0.0.0.0:34600/'

    total_request_time = 0
    request_counter = 0

    for i in range(0, 50):
        request_id = uuid.uuid1()
        request_start = datetime.datetime.now()

        operation = random.choice(operations)
        if operation == 'search':
            topic = random.choice(topics)

            # query_url = edLab_url + '/' + str(operation) + '/' + str(topic)
            query_url = local_url + '/' + str(operation) + '/' + str(topic)

            request_result = requests.get(url=query_url, data={'request_id': request_id})
            file = open("client_2_output.txt", "a+")
            file.write(request_result.text)
            file.close()
            request_end = datetime.datetime.now()
            request_time = request_end - request_start
            total_request_time = total_request_time + (request_time.microseconds / 1000)
            request_counter = request_counter + 1
            file = open("client_2_metrics.txt", "a+")
            file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
            file.close()

        elif operation == 'lookup' or 'buy':
            item = random.choice(items)

            # query_url = edLab_url + '/' + str(operation) + '/' + str(item)
            query_url = local_url + '/' + str(operation) + '/' + str(item)

            request_result = requests.get(url=query_url, data={'request_id': request_id})
            file = open("client_2_output.txt", "a+")
            file.write(request_result.text)
            file.close()
            request_end = datetime.datetime.now()
            request_time = request_end - request_start
            total_request_time = total_request_time + (request_time.microseconds / 1000)
            request_counter = request_counter + 1
            file = open("client_2_metrics.txt", "a+")
            file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
            file.close()

    file = open("client_2_metrics.txt", "a+")
    file.write("Average request processing time: {}\n".format(total_request_time / request_counter))
    file.write("End to end request processing time: {}\n".format(total_request_time))
    file.close()


if __name__ == '__main__':

    t1 = threading.Thread(target=client_1)
    t2 = threading.Thread(target=client_2)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    print("done running test 5")
