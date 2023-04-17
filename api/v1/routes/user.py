from tools.extensions import db
from tools.data_tools import generate_uuid, generate_password
from models.user import User
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required

user = Blueprint('user', __name__)

@user.route('/user', methods=['GET'])
@jwt_required()
def get_all_users():
    users = User.query.all()
    output = []
    for user in users:
        user_data = {}
        user_data['user_id'] = user.user_id
        user_data['firstname'] = user.firstname
        user_data['lastname'] = user.lastname
        user_data['userimage'] = user.userimage
        user_data['username'] = user.username
        user_data['email'] = user.email
        output.append(user_data)
    return jsonify({'users': output})

@user.route('/user', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    password_hash, salt = generate_password(data['password'])
    new_user = User(
        user_id=str(generate_uuid()),
        firstname=data['firstname'],
        lastname=data['lastname'],
        userimage=data['userimage'],
        username=data['username'],
        email=data['email'],
        password=password_hash,
        salt=salt
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'})

@user.route('/user/<user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'})
    user_data = {}
    user_data['user_id'] = user.user_id
    user_data['firstname'] = user.firstname
    user_data['lastname'] = user.lastname
    user_data['userimage'] = user.userimage
    user_data['username'] = user.username
    user_data['email'] = user.email
    return jsonify({'user': user_data})

@user.route('/user/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'})
    
    data = request.get_json()
    if data['password'] in data:
       password_hash, salt = generate_password(data['password'])
       user.password = password_hash
       user.salt = salt
    user.firstname = data['firstname']
    user.lastname = data['lastname']
    user.userimage = data['userimage']
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@user.route('/user/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'})

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User removed successfully!'})
