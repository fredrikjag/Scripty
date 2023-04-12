from functools import wraps
from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import create_access_token, JWTManager, jwt_required, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
import datetime
import tools

env_host, env_port, env_database, env_user, env_password = tools.get_sql_env()
env_app_secret = tools.get_app_env()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{env_user}:{env_password}@{env_host}:{env_port}/{env_database}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = env_app_secret
db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    password_hash, salt, user_id  = tools.get_hash(username)
    result = tools.verify_password(password, password_hash, salt)

    if result == True:
        access_token = create_access_token(identity=user_id)
        return jsonify({'access_token': access_token}), 200
    return make_response('Bad login!', 200)

# CRUD Users -------------------------------------------
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.String(36), primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    userimage = db.Column(db.String(255))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    salt = db.Column(db.String(255))

    def __init__(self, user_id, firstname, lastname, userimage, username, email, password, salt):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.userimage = userimage
        self.username = username
        self.email = email
        self.password = password
        self.salt = salt

    def __repr__(self):
        return f"<User {self.firstname} {self.lastname}>"

@app.route('/user', methods=['GET'])
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

@app.route('/user', methods=['POST'])
@jwt_required()
def create_user():
    data = request.get_json()
    password_hash, salt = tools.generate_password(data['password'])
    new_user = User(
        user_id=str(tools.generate_uuid()),
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

@app.route('/user/<user_id>', methods=['GET'])
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

@app.route('/user/<user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'})
    
    data = request.get_json()
    if data['password'] in data:
       password_hash, salt = tools.generate_password(data['password'])
       user.password = password_hash
       user.salt = salt
    user.firstname = data['firstname']
    user.lastname = data['lastname']
    user.userimage = data['userimage']
    user.username = data['username']
    user.email = data['email']
    db.session.commit()
    return jsonify({'message': 'User updated successfully!'})

@app.route('/user/<user_id>', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if not user:
        return jsonify({'message': 'User not found'})

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User removed successfully!'})

# CRUD Scripts -------------------------------------------
class Script(db.Model):
    __tablename__ = 'scripts'
    script_id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    version = db.Column(db.String(20))
    created = db.Column(db.TIMESTAMP)
    created_by = db.Column(db.String(36), db.ForeignKey('users.user_id'))
    modified = db.Column(db.TIMESTAMP)
    last_used = db.Column(db.TIMESTAMP)
    schedule_time = db.Column(db.TIMESTAMP)
    scriptfile = db.Column(db.Text)

    def __init__(self, script_id, name, description, version, created, created_by, modified, last_used, schedule_time, scriptfile):
        self.script_id = script_id
        self.name = name
        self.description = description
        self.version = version
        self.created = created
        self.created_by = created_by
        self.modified = modified
        self.last_used = last_used
        self.schedule_time = schedule_time
        self.scriptfile = scriptfile

    def to_dict(self):
        return {
            'script_id': self.script_id,
            'name': self.name,
            'description': self.description,
            'version': self.version,
            'created': self.created,
            'created_by': self.created_by,
            'modified': self.modified,
            'last_used': self.last_used,
            'schedule_time': self.schedule_time,
            'scriptfile': self.scriptfile
        }

@app.route('/script', methods=['GET'])
@jwt_required()
def get_all_scripts():
    scripts = Script.query.all()
    output = [script.to_dict() for script in scripts]
    return jsonify({'scripts': output})

@app.route('/script', methods=['POST'])
@jwt_required()
def create_script():
    data = request.get_json()
    current_user = get_jwt_identity()
    new_script = Script(
        script_id=str(tools.generate_uuid()),
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

@app.route('/script/<script_id>', methods=['GET'])
@jwt_required()
def get_script(script_id):
    script = Script.query.filter_by(script_id=script_id).first()
    if not script:
        return jsonify({'message': 'Script not found'})
    return jsonify({'script': script.to_dict()})

@app.route('/script/<script_id>', methods=['PUT'])
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

@app.route('/script/<script_id>', methods=['DELETE'])
@jwt_required()
def delete_script(script_id):
    script = Script.query.filter_by(script_id=script_id).first()
    if not script:
        return jsonify({'message': 'Script not found'})
    
    db.session.delete(script)
    db.session.commit()
    return jsonify({'message': 'Script deleted successfully!'})

# CRUD Pieplines -------------------------------------------
class Pipeline(db.Model):
    __tablename__ = 'pipelines'
    pipe_id = db.Column(db.String(36), primary_key=True)
    script_id = db.Column(db.String(36), db.ForeignKey('scripts.script_id'))
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    version = db.Column(db.String(20))
    created = db.Column(db.TIMESTAMP)
    created_by = db.Column(db.String(36), db.ForeignKey('users.user_id'))
    modified = db.Column(db.TIMESTAMP)
    last_used = db.Column(db.TIMESTAMP)
    schedule_time = db.Column(db.TIMESTAMP)

    def __init__(self, pipe_id, script_id, name, description, version, created, created_by, modified, last_used, schedule_time):
        self.pipe_id = pipe_id
        self.script_id = script_id
        self.name = name
        self.description = description
        self.version = version
        self.created = created
        self.created_by = created_by
        self.modified = modified
        self.last_used = last_used
        self.schedule_time = schedule_time

    def __repr__(self):
        return f"<Pipeline {self.name} {self.version}>"

@app.route('/pipeline', methods=['GET'])
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

@app.route('/pipeline', methods=['POST'])
@jwt_required()
def create_pipeline():
    data = request.get_json()
    new_pipeline = Pipeline(
        pipe_id=str(tools.generate_uuid()),
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

@app.route('/pipeline/<pipe_id>', methods=['GET'])
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

@app.route('/pipeline/<pipe_id>', methods=['PUT'])
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
    pipeline.schedule_time = data.get('schedule_time')
    db.session.commit()
    return jsonify({'message': 'Pipeline updated successfully!'})

@app.route('/pipeline/<pipe_id>', methods=['DELETE'])
@jwt_required()
def delete_pipeline(pipe_id):
    pipeline = Pipeline.query.filter_by(pipe_id=pipe_id).first()
    if not pipeline:
        return jsonify({'message': 'Pipeline not found'})
    
    db.session.delete(pipeline)
    db.session.commit()
    return jsonify({'message': 'Pipeline deleted successfully!'})

# CRUD Pipe_Scripts -------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5000)
