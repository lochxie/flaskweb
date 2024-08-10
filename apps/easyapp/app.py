import os
from flask_mail import Mail, Message
from flask import Flask, render_template, url_for, request, redirect, flash
from email_validator import validate_email, EmailNotValidError

app = Flask(__name__)

app.config["SECRET_KEY"] = b'\xb1\xa5SU\xfc\x16\xa7p\xabj\xe1\xbfr\x94h\xdd'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'jojju486@gmail.com'
app.config['MAIL_PASSWORD'] = 'stkm cgck saeq hlju'

mail = Mail(app)

@app.route("/")
def index():
    return 'hello, flaskweb'

@app.route("/hello/<name>", methods=["GET"], endpoint="hello-endpoint")
def hello(name):
    return f"hello {name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

def send_email(to, subject, template, **kwargs):    
    msg = Message(subject, sender='jojju486@gmail.com', recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contact/complete', methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not username:
            flash("사용자명은 필수입니다.")
            is_valid = False

        if not email:
            flash("메일주소는 필수입니다.")
            is_valid = False
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일주소의 형식으로 입력하세요.")
            is_valid = False

        if not description:
            flash("문의 내용은 필수입니다.")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))
        
        send_email(
            email,
            "문의 감사합니다.",
            "contact_mail",
            username = username,
            description = description
        )
        flash("문의 내용은 메일로 송신되었습니다. 문의해 주셔서 감사합니다.")

        return redirect(url_for('contact_complete'))
    return render_template("contact_complete.html")
