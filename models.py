from flask_sqlalchemy import SQLAlchemy
import datetime
from alembic import op


db = SQLAlchemy()


class BaseModel(db.Model):
    __abstract__ = True

    def __init__(self, *args):
        super().__init__(*args)

    def __repr__(self):
        return '%s(%s)' % (self.__class__.__name__, {
            column: value
            for column, value in self._to_dict().items()
        })

    def json(self):
        return {
            column: value if not isinstance(value, datetime.date) else value.strftime('%Y-%m-%d')
            for column, value in self._to_dict().items()
        }


class SensorDataModel(BaseModel):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    accX = db.Column(db.Float)
    accY = db.Column(db.Float)
    accZ = db.Column(db.Float)
    gyroX = db.Column(db.Float)
    gyroY = db.Column(db.Float)
    gyroZ = db.Column(db.Float)
    magX = db.Column(db.Float)
    magY = db.Column(db.Float)
    magZ = db.Column(db.Float)

    def __init__(self, data, *args):
        super().__init__(*args)
        self.time = datetime.datetime.fromtimestamp(data.get('time')/1e3)
        self.accX = data.get('accX')
        self.accY = data.get('accY')
        self.accZ = data.get('accZ')
        self.gyroX = data.get('gyroX')
        self.gyroY = data.get('gyroY')
        self.gyroZ = data.get('gyroZ')
        self.magX = data.get('magX')
        self.magY = data.get('magY')
        self.magZ = data.get('magZ')

    def save(self):
        db.session.add(self)
        db.session.commit()
