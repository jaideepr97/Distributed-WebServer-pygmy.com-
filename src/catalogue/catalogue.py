from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields
import threading
import datetime
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
db = SQLAlchemy(app)
buy_lock = threading.Lock()
log_lock = threading.Lock()


class Catalog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Float, nullable=False)
    topic = db.Column(db.String(100), nullable=False)


class CatalogSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()
    quantity = fields.Int()
    cost = fields.Float()
    topic = fields.Str()


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/query_by_subject/<args>', methods=["GET"])
def query_by_subject(args):

    request_start = datetime.datetime.now()
    request_id = request.values['request_id']

    catalogs_schema = CatalogSchema(many=True)
    catalogs = Catalog.query.with_entities(Catalog.name, Catalog.id).filter_by(topic=args.lower()).all()
    result = catalogs_schema.dump(catalogs)

    request_end = datetime.datetime.now()
    request_time = request_end - request_start

    log_lock.acquire()
    file = open("catalog_server.txt", "a+")
    file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
    file.close()
    log_lock.release()

    return {'results': result}


@app.route('/query_by_item/<int:args>', methods=["GET"])
def query_by_item(args):

    request_start = datetime.datetime.now()
    request_id = request.values['request_id']

    catalog_schema = CatalogSchema()
    catalog = Catalog.query.with_entities(Catalog.name, Catalog.quantity, Catalog.cost).filter_by(id=args).first()
    result = catalog_schema.dump(catalog)

    request_end = datetime.datetime.now()
    request_time = request_end - request_start

    log_lock.acquire()
    file = open("catalog_server.txt", "a+")
    file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
    file.close()
    log_lock.release()

    return {'result': result}


@app.route('/update/<int:args>', methods=["GET"])
def update(args):

    request_start = datetime.datetime.now()
    request_id = request.values['request_id']

    buy_lock.acquire()
    catalog = db.session.query(Catalog).filter_by(id=args).with_for_update().first()
    if catalog is not None and catalog.quantity > 0:
        catalog.quantity -= 1
        db.session.commit()
        buy_lock.release()

        request_end = datetime.datetime.now()
        request_time = request_end - request_start

        log_lock.acquire()
        file = open("front_end_server.txt", "a+")
        file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
        file.close()
        log_lock.release()

        return {'result': 0, 'remaining_stock': catalog.quantity}
    else:
        db.session.commit()
        buy_lock.release()

        request_end = datetime.datetime.now()
        request_time = request_end - request_start

        log_lock.acquire()
        file = open("front_end_server.txt", "a+")
        file.write("{} \t\t\t {}\n".format(request_id, (request_time.microseconds / 1000)))
        file.close()
        log_lock.release()

        return {'result': -1}


@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34602, debug=True)
