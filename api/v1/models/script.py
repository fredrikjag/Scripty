from tools.extensions import db


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