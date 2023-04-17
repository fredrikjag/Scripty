from tools.extensions import db


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