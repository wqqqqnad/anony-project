from datetime import datetime

from apps.app import db
from werkzeug.security import generate_password_hash


class User(db.Model):

    __tablename__= "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String) # 123 => ㅈ기ㅓㅗㅁㄴ어ㅗㄹ
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(
        db.DateTime, default=datetime.now, onupdate=datetime.now
    )
    

    #  속성값 getter
    @property
    def password(self):
        raise AttributeError("일어 들일 수 없음")
    
    #  속성값 setter
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)