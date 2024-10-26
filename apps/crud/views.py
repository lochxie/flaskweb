from flask import Flask, Blueprint, render_template, redirect, url_for
from app import db
from apps.crud.models import User
from apps.crud.forms import UserForm
from flask_login import login_required

#Blueprint로 crud앱을 생성
crud = Blueprint(
    "crud", 
    __name__,
    template_folder="templates",
    static_folder="static"
)

@crud.route("/")
@login_required
def index():
    return render_template("crud/index.html")

@crud.route("/sql")
@login_required
def sql():
    #user = User(
    #    username = '김',
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

@crud.route('/users/new',methods=["GET","POST"])
@login_required
def create_user():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password_hash = form.password.data
        )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("crud.users"))
    return render_template("crud/create.html", form=form)

@crud.route('/users')
@login_required
def users():
    users = User.query.all()
    return render_template('crud/index.html', users=users)

@crud.route('/user/<user_id>',methods=["GET","POST"])
@login_required
def edit_user(user_id):
    form = UserForm()
    user = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password_hash = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('crud.users'))  
    return render_template('crud/edit.html', user=user, form=form)

@crud.route('/user/<user_id>/delete',methods=["POST"])
@login_required
def delete_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('crud.users'))