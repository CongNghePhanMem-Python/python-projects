from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user

from QLHS import app, login
from QLHS.AddViewAdmin.AddViewClass import ClassCustomizes
from QLHS.AddViewAdmin.AddViewStudent import StudentCustomize
from QLHS.AddViewAdmin.AddViewGrade import GradeCustomizes
from QLHS.AddViewAdmin.AddViewSemester import SemesterCustomize
from QLHS.AddViewAdmin.AddViewMark import MarkCustomizes
from QLHS.AddViewAdmin.AddViewSubject import SubjectCustomize
from QLHS.AddViewAdmin.AddViewGpa import *
from QLHS.Logout.AddViewLogout import LogoutView
from QLHS.Register.AddViewRegister import RegisterView

from QLHS.models import User
import hashlib


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login-admin", methods=['Post', 'Get'])
def login_admin():
    if request.method == "POST":
        user_name = request.form.get("username")
        password = request.form.get("password", "")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        user = User.query.filter(User.user_name == user_name.strip(), User.password == password).first()
        if user:
            login_user(user=user)

    return redirect("/admin")


@app.route("/register-admin", methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        user_name = request.form.get("username")
        name = request.form.get("name")
        password = request.form.get("password", "")
        confirmpassword = request.form.get("confirmpassword", "")
        email = request.form.get("email")
        password = str(hashlib.md5(password.strip().encode("utf-8")).hexdigest())
        confirmpassword =str(hashlib.md5(confirmpassword.strip().encode("utf-8")).hexdigest())
        if password != confirmpassword:
            flash('Password not same.')
            return redirect(url_for('sign_up'))
        user = User.query.filter(User.email == email).first()
        if user:
            flash('Email address already exist.')
            return redirect(url_for('registerview.__index__'))
        new_user = User(name=name, user_name=user_name, email=email, password=password, active=1)
        db.session.add(new_user)
        db.session.commit()
    return redirect(url_for('login_admin'))



@login.user_loader
def User_load(user_id):
    return User.query.get(user_id)


if __name__ == "__main__":
    app.run(debug=True)
