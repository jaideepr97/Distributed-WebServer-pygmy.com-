from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catalog.db'
db = SQLAlchemy(app)


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


@app.route('/query_by_subject/<args>', methods=["GET"])
def query_by_subject(args):
    catalogs_schema = CatalogSchema(many=True)
    catalogs = Catalog.query.with_entities(Catalog.name, Catalog.id).filter_by(topic=args.lower()).all()
    result = catalogs_schema.dump(catalogs)
    return {'results': result}


@app.route('/query_by_item/<int:args>', methods=["GET"])
def query_by_item(args):
    catalog_schema = CatalogSchema()
    catalog = Catalog.query.with_entities(Catalog.quantity, Catalog.cost).filter_by(id=args).first()
    result = catalog_schema.dump(catalog)
    return {'result': result}


@app.route('/update/<int:args>', methods=["GET"])
def update(args):
    catalog_schema = CatalogSchema()
    catalog = Catalog.query.filter_by(id=args).first()
    if catalog is not None and catalog.quantity > 0:
        catalog.quantity -= 1
        db.session.commit()
        return {'result': 0}
    else:
        return {'result': -1}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34602, debug=True)
