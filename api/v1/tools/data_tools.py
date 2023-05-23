import uuid
import bcrypt
import os
import psycopg2
from dotenv import load_dotenv


def get_sql_env():
    load_dotenv()
    env_host = os.getenv('host')
    env_port = os.getenv('port')
    env_database = os.getenv('database')
    env_user = os.getenv('user')
    env_password = os.getenv('password')
    return env_host, env_port, env_database, env_user, env_password

def get_app_env():
    load_dotenv()
    env_app_secret = os.getenv('jwt_key')
    return env_app_secret

# Generates UUID
def generate_uuid():
    return uuid.uuid4().hex

def generate_password(password):
    salt = bcrypt.gensalt()
    password_hash = (bcrypt.hashpw(password.encode('utf-8'), salt)).decode()
    salt = salt.decode()
    return password_hash, salt

def verify_password(password, password_hash, salt):
    user_password = (bcrypt.hashpw(password.encode('utf-8'), salt.encode())).decode()
    if user_password == password_hash:
        return True
    return False

def get_hash(username):
    env_host, env_port, env_database, env_user, env_password = get_sql_env()
    with psycopg2.connect(
        host=env_host,
        port=env_port,
        database=env_database,
        user=env_user,
        password=env_password
    ) as conn: 
        with conn.cursor() as cur:
            cur.execute('''
                SELECT password, salt, user_id, username FROM Users WHERE username = %s; 
            ''',(username,))
            password_hash, salt, user_id, user = cur.fetchone()
    return password_hash, salt, user_id, user


if __name__ == "__main__":
    print("Tools")