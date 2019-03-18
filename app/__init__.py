from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['SECRET_KEY'] = "M73ei896e4AnShEOCC1lDw"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tpyjaxxbqgmate:557fc25fd481065aaa71d6b1fb3c5e1fedf663ea37d755a4e243a6fc266c998b@ec2-54-197-232-203.compute-1.amazonaws.com:5432/da5vvkc79euvvu'


db = SQLAlchemy(app)



app.config.from_object(__name__)
from app import views

