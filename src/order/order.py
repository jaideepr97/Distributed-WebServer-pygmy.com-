from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import random
import string
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app)


class Order(db.Model):
    id = db.Column(db.String(16), primary_key=True)
    item_number = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())


class OrderSchema(Schema):
    id = fields.Str(dump_only=True)
    item_number = fields.Int()
    total_price = fields.Float()
    date_created = fields.DateTime()


@app.route('/buy/<int:args>')
def buy(args):
    query_url = 'http://elnux1.cs.umass.edu:34602/query_by_item/'+str(args)
    query_result = requests.get(url=query_url)
    query_data = query_result.json()
    if query_data is not None and query_data['result']['quantity'] > 0:
        update_url = 'http://elnux1.cs.umass.edu:34602/update/'+str(args)
        update_result = requests.get(url=update_url)
        update_data = update_result.json()
        if update_data['result'] == 0:
            _id = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
            order = Order(id=_id, item_number=args, total_price=query_data['result']['cost'])
            db.session.add(order)
            db.session.commit()
            order_details = Order.query.filter_by(id=_id).first()
            order_schema = OrderSchema()
            result = order_schema.dump(order_details)
            return {'Buy Successful': result}
        else:
            return 'Buy Failed!'
    else:
        return 'Buy Failed!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34601, debug=True)
