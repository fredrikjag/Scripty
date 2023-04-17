from flask import Flask
from tools.extensions import db, jwt
from tools.data_tools import get_sql_env, get_app_env
from routes import auth, pipeline, script, user

def create_app():
    env_host, env_port, env_database, env_user, env_password = get_sql_env()
    env_app_secret = get_app_env()

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{env_user}:{env_password}@{env_host}:{env_port}/{env_database}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = env_app_secret

    db.init_app(app)
    jwt.init_app(app)
    
    app.register_blueprint(auth, url_prefix='/api/d')
    app.register_blueprint(pipeline, url_prefix='/api/d')
    app.register_blueprint(script, url_prefix='/api/d')
    app.register_blueprint(user, url_prefix='/api/d')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
