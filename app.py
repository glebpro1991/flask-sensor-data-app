from flask import Flask, render_template, request
from models import db, SensorDataModel

app = Flask(__name__)



POSTGRES = {
    'user': 'srqqtgrpbtauoh',
    'pw': 'ed84051e3ee744aed0024048731bcfc17b709b6f4d3c44609beb71587b19b75b',
    'db': 'd7etse1b52ls3r',
    'host': 'ec2-54-243-187-30.compute-1.amazonaws.com',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


db.init_app(app)


@app.route('/', methods=['GET'])
def present():
    return "Hello darkness my old friend!"


# first endpoint
@app.route('/save', methods=['POST'])
def save():
    req_data = request.get_json()
    sensor_data = SensorDataModel(req_data)
    sensor_data.save()
    return 'OK'


if __name__ == '__main__':
    app.run(debug=True)