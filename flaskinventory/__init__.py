from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '323b22caac41acbf'
app.config['SQLALCHEMY'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
db = SQLAlchemy(app)

from flaskinventory import routes

db.create_all()
db.session.commit()
