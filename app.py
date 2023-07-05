from flask import Flask, request, jsonify
from gunicorn.app.base import BaseApplication
from multiprocessing import Process

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not is_valid_username(username):
        return jsonify({'message': 'Invalid username'}), 400

    if not is_valid_password(password):
        return jsonify({'message': 'Invalid password'}), 400

    return jsonify({'message': 'Login successful'}), 200

def is_valid_username(username):
    if not username.isalnum():
        return False

    if not 6 <= len(username) <= 12:
        return False

    return True

def is_valid_password(password):
    if len(password) < 6:
        return False

    return True

class GunicornApp(BaseApplication):
    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        config = {
            key: value for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application

if __name__ == '__main__':
    options = {
        'bind': '127.0.0.1:5000',
        'workers': 4
    }
    GunicornApp(app, options).run()
