from tools.extensions import db
from tools.data_tools import generate_uuid
from models.script import Script
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime
import os 

script = Blueprint('script', __name__)

@script.route('/script', methods=['GET'])
@jwt_required()
def get_all_scripts():
    scripts = Script.query.all()
    output = [script.to_dict() for script in scripts]
    return jsonify({'scripts': output})

@script.route('/script', methods=['POST'])
@jwt_required()
def create_script():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_script = Script(
        script_id=str(generate_uuid()),
        name=data['name'],
        description=data['description'],
        version=data['version'],
        created=datetime.datetime.now(),
        created_by=current_user,
        modified=None,
        last_used=None,
        schedule_time=None,
        scriptfile=data['scriptfile']
    )
    db.session.add(new_script)
    db.session.commit()
    return jsonify({'message': 'Script created successfully!'})

@script.route('/script/<script_id>', methods=['GET'])
@jwt_required()
def get_script(script_id):
    script = Script.query.filter_by(script_id=script_id).first()
    if not script:
        return jsonify({'message': 'Script not found'})
    return jsonify({'script': script.to_dict()})

@script.route('/script/<script_id>', methods=['PUT'])
@jwt_required()
def update_script(script_id):
    script = Script.query.filter_by(script_id=script_id).first()
    if not script:
        return jsonify({'message': 'Script not found'})
    
    data = request.get_json()
    script.name = data['name']
    script.description = data['description']
    script.version = data['version']
    script.modified = datetime.datetime.now()
    db.session.commit()
    return jsonify({'message': 'Script updated successfully!'})

@script.route('/script/<script_id>', methods=['DELETE'])
@jwt_required()
def delete_script(script_id):
    script = Script.query.filter_by(script_id=script_id).first()
    if not script:
        return jsonify({'message': 'Script not found'})
    
    db.session.delete(script)
    db.session.commit()
    return jsonify({'message': 'Script deleted successfully!'})



##### Script upload


@script.route('/script/upload', methods=['POST'])
@jwt_required()
def script_upload():
    if 'file' not in request.files:
        return jsonify({'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    upload_directory = './files'
    file.save(os.path.join(upload_directory, file.filename))

    return jsonify({'message': 'File uploaded successfully'})