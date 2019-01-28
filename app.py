from flask import Flask, request, jsonify
from models import db, SensorDataModel
import json

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


# Home page just prints the message
@app.route('/', methods=['GET'])
def home():
    return "Successfully deployed"


# Save endpoint
@app.route('/save', methods=['POST'])
def save():
    req_data = request.get_json()
    json_string = req_data.read()
    data = json.loads(json_string)
    isValidBatch(data)
    return jsonify([{"status": "ok"}])


def isValidBatch(data):
    for key in data:
        item = data[key]
        if len(item) != 100:
            raise Exception('Batch does not contain 100 records. It only contains ' + len(item) + ' elements')
        for i, item in enumerate(item):
            index = str(i)
            id1 = item['sampleId']
            if len(index) == 1:
                id2 = str(key) + '0' + index
            else:
                id2 = str(key) + index

            if int(id1) != int(id2):
                raise Exception('Inconsistencies in sample IDs: ' + str(id1) + ' ' + str(id2))
    print("Samples are consistent with the batch. No inconsistencies found")


def saveData(data):
    try:
        db.session.begin()
        db.session.add_all(
            [
                SensorDataModel(record)
                for record in data
            ]
        )
        db.session.commit()
    except Exception as e:
        print("Exception type: " + str(e))
        db.session.rollback()
        return False
    else:
        return True
    finally:
        db.session.close()


if __name__ == '__main__':
    app.run(debug=True)
