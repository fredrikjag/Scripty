from tools.extensions import db
from tools.data_tools import generate_uuid
from models.pipeline import Pipeline
from flask import jsonify, request, Blueprint
from flask_jwt_extended import jwt_required, get_jwt_identity
import datetime

pipeline = Blueprint('pipeline', __name__)

@pipeline.route('/pipeline', methods=['GET'])
@jwt_required()
def get_all_pipelines():
    pipelines = Pipeline.query.all()
    output = []
    for pipeline in pipelines:
        pipeline_data = {}
        pipeline_data['pipe_id'] = pipeline.pipe_id
        pipeline_data['script_id'] = pipeline.script_id
        pipeline_data['name'] = pipeline.name
        pipeline_data['description'] = pipeline.description
        pipeline_data['version'] = pipeline.version
        pipeline_data['created'] = pipeline.created
        pipeline_data['created_by'] = pipeline.created_by
        pipeline_data['modified'] = pipeline.modified
        pipeline_data['last_used'] = pipeline.last_used
        pipeline_data['schedule_time'] = pipeline.schedule_time
        output.append(pipeline_data)
    return jsonify({'pipelines': output})

@pipeline.route('/pipeline', methods=['POST'])
@jwt_required()
def create_pipeline():
    data = request.get_json()
    new_pipeline = Pipeline(
        pipe_id=str(generate_uuid()),
        script_id=data['script_id'],
        name=data['name'],
        description=data['description'],
        version=data['version'],
        created=datetime.datetime.now(),
        created_by=get_jwt_identity(),
        modified=datetime.datetime.now(),
        last_used=None,
        schedule_time=None
    )
    db.session.add(new_pipeline)
    db.session.commit()
    return jsonify({'message': 'Pipeline created successfully!'})

@pipeline.route('/pipeline/<pipe_id>', methods=['GET'])
@jwt_required()
def get_pipeline(pipe_id):
    pipeline = Pipeline.query.filter_by(pipe_id=pipe_id).first()
    if not pipeline:
        return jsonify({'message': 'Pipeline not found'})
    pipeline_data = {}
    pipeline_data['pipe_id'] = pipeline.pipe_id
    pipeline_data['script_id'] = pipeline.script_id
    pipeline_data['name'] = pipeline.name
    pipeline_data['description'] = pipeline.description
    pipeline_data['version'] = pipeline.version
    pipeline_data['created'] = pipeline.created
    pipeline_data['created_by'] = pipeline.created_by
    pipeline_data['modified'] = pipeline.modified
    pipeline_data['last_used'] = pipeline.last_used
    pipeline_data['schedule_time'] = pipeline.schedule_time
    return jsonify({'pipeline': pipeline_data})

@pipeline.route('/pipeline/<pipe_id>', methods=['PUT'])
@jwt_required()
def update_pipeline(pipe_id):
    pipeline = Pipeline.query.filter_by(pipe_id=pipe_id).first()
    if not pipeline:
        return jsonify({'message': 'Pipeline not found'})
    
    data = request.get_json()
    pipeline.name = data['name']
    pipeline.description = data['description']
    pipeline.version = data['version']
    pipeline.modified = datetime.now()
    pipeline.schedule_time = pipeline.get('schedule_time')
    db.session.commit()
    return jsonify({'message': 'Pipeline updated successfully!'})

@pipeline.route('/pipeline/<pipe_id>', methods=['DELETE'])
@jwt_required()
def delete_pipeline(pipe_id):
    pipeline = Pipeline.query.filter_by(pipe_id=pipe_id).first()
    if not pipeline:
        return jsonify({'message': 'Pipeline not found'})
    
    db.session.delete(pipeline)
    db.session.commit()
    return jsonify({'message': 'Pipeline deleted successfully!'})