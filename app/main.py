import os
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from flask_apscheduler import APScheduler
from tickets import *

class Config(object):
    JOBS = [{
        'id': 'job1',
        'func': get_users_tickets,
        'trigger': 'interval',
        'hours': 24
    }]

app = Flask(__name__, static_folder='static/static')
app.config.from_object(Config())


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


def _ok_message(data, message = ''):
    return jsonify({
        'status': 'ok',
        'message': message,
        'data': data
    }), 200


def _fail_message(message = ''):
    return jsonify({
        'status': 'fail',
        'message': message,
        'data': {}
    }), 400


@app.route('/api')
def index():
    return _ok_message({}, 'API live')


@app.route('/api/all')
def all():
    return _ok_message(get_users_tickets())


@app.route('/api/ticket', methods=['POST'])
def ticket():
    #request.values
    try:
        plate = request.json['data']['plate'].upper()
        serial = request.json['data']['serial']
        email = request.json['data']['email'].lower()
        update = request.json['data']['update']
    except:
        return _fail_message('Bad request format.')

    if not plate or not serial or not email:
        return _fail_message('Bad request format.')

    save_user(plate, serial, email, update)

    return _ok_message(get_user_tickets(plate, serial))


@app.route('/')
def main():
    index_path = os.path.join('/app/static', 'index.html')
    return send_file(index_path)


@app.route('/<path:path>')
def route_frontend(path):
    file_path = os.path.join(app.static_folder, path)
    if os.path.isfile(file_path):
        return send_file(file_path)
    else:
        index_path = os.path.join('/app/static', 'index.html')
        return send_file(index_path)


if __name__ == '__main__':
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=False, port=80)
