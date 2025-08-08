from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
db = SQLAlchemy(app)
api = Api(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"


user_args = reqparse.RequestParser()
user_args.add_argument("username", type=str, help="Username of the user", required=True)
user_args.add_argument("email", type=str, help="Email of the user", required=True)
@app.route("/")
def home():
    return "<h1>WELCOME TO MY WORLD</h1>"

if __name__ == "__main__":
    app.run(debug=True)
