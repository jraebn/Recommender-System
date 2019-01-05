from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:carrotcake092814@localhost/BookDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

import models

db.create_all()

from app import controller
app.debug= True