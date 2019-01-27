from flask import Flask, request, jsonify
from models import db, SensorDataModel
import queue

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

q = queue.Queue()


# Home page just prints the message
@app.route('/', methods=['GET'])
def home():
    return "Successfully deployed"


# Save endpoint
@app.route('/save', methods=['POST'])
def save():
    req_data = request.get_json()
    q.put(req_data)
    print(q.qsize())

    saveData(q.get())
    q.join()

    if q.task_done():
        return jsonify([{"status": "ok"}])
    else:
        return jsonify([{"status": "fail"}])


def saveData(data):
    try:
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
