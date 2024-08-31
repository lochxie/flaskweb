from flask import Flask, Blueprint, render_template, redirect,url_for
from apps.app import db
from apps.crud.models import User
from apps.crud.forms import UserForm

#Blueprint로 crud앱을 생성
crud = Blueprint(
    "crud", __name__,
    template_folder="templates",
    static_folder="static"
)

@crud.route("/")
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
def sql():
    #user = User(
    #    username = '김소연',
    #    email = 'lochxie@naver.com',
    #    userid = 'rla',
    #    password_hash = '1111'
    #)
    #db.session.add(user) #사용자 추가
    #db.session.commit() #commit하기
    #db.session.query(User).all()
    #db.session.query(User).filter_by(id=1)
    db.session.query(User).filter_by(id=2).delete()
    db.session.commit()
    return '콘솔 로그 확인'

@crud.route('/user/new',methods=["GET","POST"])
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)