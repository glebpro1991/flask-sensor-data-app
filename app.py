from flask import Flask, request, jsonify
from models import db, SensorDataModel

app = Flask(__name__)

POSTGRES = {
    'user': 'srqqtgrpbtauoh',
    'pw': 'b080181b42c55e240367b85a165d5684c9ce2171ea9c3f0c13e41698cbc8afe1',
    'db': 'd7etse1b52ls3r',
    'host': 'ec2-54-243-187-30.compute-1.amazonaws.com',
    'port': '5432',
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

db.init_app(app)


@app.route('/', methods=['GET'])
def home():
    return "Successfully deployed"


# Save endpoint
@app.route('/save', methods=['POST'])
def save():
    req_data = request.get_json()
    for record in req_data:
        sensor_data = SensorDataModel(record)
        response = sensor_data.save()
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
