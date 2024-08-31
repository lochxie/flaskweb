from datetime import datetime
from apps.app import db
from werkzeug.security import generate_password_hash

#de.Model을 상속한 클래스 작성
class User(db.Model):
    __tabelname__="users"
    #Column명 정의
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, index=True)
    #userid = db.Column(db.String, index=True)
    password = db.Column(db.String)
    create_at = db.Column(db.DateTime, default=datetime.now)
    update_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    @property
    def password(self):
        raise AttributeError('비밀번호를 입력하세요')
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash

