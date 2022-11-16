from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
#conectivity with PostGress
app.config['SECRET_KEY'] = 'thisissecret'
# our database uri
hostname = "ec2-52-204-157-26.compute-1.amazonaws.com"
username = "vwlybnwovcwsol"
password = "31c56e9873952b5f0f1ec89620b25ed2a3492ce015b21405f2dec73db602c890"
dbname = "d58qba9h8gin2r"


app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{hostname}:5432/{dbname}"
print(f"postgresql://{username}:{password}@{hostname}:5432/{dbname}")

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

# Create A Model For Table
class BlogPosts(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(1000))
    blog_description = db.Column(db.String(6000))    

if __name__ == '__main__':
    with app.app_context():
        db.create_all() # <--- create db object.
    app.run(debug=True)