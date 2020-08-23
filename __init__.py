from flask import Flask
from flask_admin import Admin
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "password"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/qlhsdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS "] = True

db = SQLAlchemy(app=app)

admin = Admin(app=app, name="Quan ly hoc sinh", template_mode="bootstrap3")
login = LoginManager(app=app)

