from tools.data_tools import get_hash, verify_password
from flask import jsonify, request, make_response, Blueprint
from flask_jwt_extended import create_access_token


auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    password_hash, salt, user_id, user = get_hash(username)
    result = verify_password(password, password_hash, salt)

    additional_claims = {"user": user}

    if result == True:
        access_token = create_access_token(identity=user_id, additional_claims=additional_claims)
        return jsonify({'access_token': access_token}), 200
    return make_response('Bad login!', 200)