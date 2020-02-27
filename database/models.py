from .db import db

class Tasks(db.Document):
    title = db.StringField(max_length=200, required=True, unique=True)
    description = db.StringField(required=False)
    done = db.BooleanField(default=False, required=True)
