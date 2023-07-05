from flask import Blueprint, request, jsonify

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not is_valid_username(username):
        return jsonify({'message': 'Invalid username'}), 400

    if not is_valid_password(password):
        return jsonify({'message': 'Invalid password'}), 400

    return jsonify({'message': 'Login successful'}), 200

def is_valid_username(username):
    return username.isalnum() and len(username) >= 6 and len(username) <= 12

def is_valid_password(password):
    return any(c.isalpha() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password) and len(password) >= 6
