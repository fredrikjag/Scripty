from tools import data_tools
import psycopg2

env_host, env_port, env_database, env_user, env_password = data_tools.get_sql_env()

# Connect to the PostgreSQL database
with psycopg2.connect(
    host=env_host,
    port=env_port,
    database=env_database,
    user=env_user,
    password=env_password
) as conn: 
    with conn.cursor() as cur:
        cur.execute('''
            CREATE TABLE Users (
                user_id TEXT PRIMARY KEY,
                firstname VARCHAR(50) NOT NULL,
                lastname VARCHAR(50) NOT NULL,
                userimage VARCHAR(255),
                username VARCHAR(50) NOT NULL UNIQUE,
                email VARCHAR(255) NOT NULL UNIQUE,
                password VARCHAR(255) NOT NULL,
                salt VARCHAR(255) NOT NULL
            );
        ''')
        conn.commit()
        
        cur.execute('''
           CREATE TABLE Scripts (
                script_id TEXT PRIMARY KEY,
                name VARCHAR(100),
                description TEXT,
                version VARCHAR(20),
                created TIMESTAMP,
                created_by TEXT REFERENCES Users(user_id),
                modified TIMESTAMP,
                last_used TIMESTAMP,
                schedule_time TIMESTAMP,
                scriptfile TEXT
            );
        ''')
        conn.commit()

        cur.execute('''
            CREATE TABLE Pipelines (
                pipe_id TEXT PRIMARY KEY,
                script_id TEXT REFERENCES Scripts(script_id),
                name VARCHAR(100),
                description TEXT,
                version VARCHAR(20),
                created TIMESTAMP,
                created_by TEXT REFERENCES Users(user_id),
                modified TIMESTAMP,
                last_used TIMESTAMP,
                schedule_time TIMESTAMP
            );
        ''')
        conn.commit()

        cur.execute('''
            CREATE TABLE Pipe_scripts (
                pipechild_id TEXT PRIMARY KEY,
                pipe_id TEXT REFERENCES Pipelines(pipe_id),
                script_id TEXT REFERENCES Scripts(script_id)
            );
        ''')
        conn.commit()

        cur.execute('''
            CREATE TABLE schedules (
                schedule_id TEXT PRIMARY KEY,
                script_id TEXT REFERENCES scripts(script_id) NULL,
                pipe_id TEXT REFERENCES pipelines(pipe_id) NULL
            );
        ''')
        conn.commit()

        user_id = data_tools.generate_uuid()
        password_hash, salt = data_tools.generate_password("Password")
        cur.execute('''
            INSERT INTO Users (user_id, firstname, lastname, username, email, password, salt)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (user_id, 'Admin', 'Scripty', 'admin', 'scripty@localhost.local', password_hash, salt))

        conn.commit()
