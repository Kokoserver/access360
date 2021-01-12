from uuid import uuid4
from datetime import datetime
from mongoengine import Document,DateField, StringField, BooleanField, EmailField

class UserAccount(Document):
    username = StringField(required=True, min_length=3)
    email = EmailField(required=True,  unique=True)
    gender = StringField(choices=("male", "female"), required=True)
    password = StringField(required=True)
    active   = BooleanField(default=True)
    admin    = BooleanField(default=True)
    created_at = DateField(default=datetime.utcnow())
    meta  = {"db_alias":"core"}

    def to_json(self, *args, **kwargs):
        return {
            "id":str(self.id),
            "username":self.username,
            "email":self.email,
            "created_at":str(self.created_at)
        }

