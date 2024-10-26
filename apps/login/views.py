from flask import Flask, Blueprint, render_template, redirect, url_for, flash, request
from app import db
from apps.crud.models import User
from apps.login.forms import SignUpForm
from flask_login import login_user, logout_user

#Blueprint로 login앱을 생성
login = Blueprint(
    "login", 
    __name__,
    template_folder="templates",
    static_folder="static"
)

@login.route("/")
def index():
    return render_template("login/index.html")

@login.route("/signup", methods=["GET","POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            password = form.password.data
        )

    #메일 중복 체크
    if user.is_duplicate_email():
        flash("이메일 주소가 이미 등록되어있습니다.")
        return redirect(url_for("login.signup"))

    #사용자 정보 등록
    db.session.add(user)
    db.session.commit()

    #사용자 정보를 세션에 저장
    login_user(user)

    next_ = request.args.get("next")
    if next_ is None and next_.startswitch("/"):
        next_ = url_for("crud.users")
    return redirect(next_)

    return render_template("login/signup.html", form=form)

#@login.route("/login",method="GET","POST")
#def login():
#    form = LoginForm