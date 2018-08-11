# -*- encoding: utf8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
from config import local_config


# DB class
app = Flask(__name__)
print local_config.DB_URI
app.config['SQLALCHEMY_DATABASE_URI'] = local_config.DB_URI
db = SQLAlchemy(app)

print('tuomatuo core init................................')