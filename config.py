from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask import Flask ,request, jsonify
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from models import db, User


app = Flask(__name__, template_folder='projecttemplate/template/',static_folder='projecttemplate/assets')
# Configure the MySQL connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/userdata'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
# db = SQLAlchemy()


###### when data modle add that time this are use in falsk project
db.init_app(app)


with app.app_context():
    db.create_all()



