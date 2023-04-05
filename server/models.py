from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True) ##not always
    image = db.Column(db.String)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'''
        id: {self.id}
        name: {self.name}
        image: {self.image}
        price: {self.price}
        '''
