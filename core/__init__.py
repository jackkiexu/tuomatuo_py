# -*- encoding: utf8 -*-
import os

import flask
from flask import Flask, request, g, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
from config import local_config
import logging
import uuid
from threading import local

thread_local = local()
root_path = os.path.dirname(os.path.abspath(__file__)) + '/../'

class RequestIDLogFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = getattr(thread_local, 'request_id', "none")
        return record


logger = logging.getLogger()
logger.setLevel(logging.INFO)    # Log等级总开关
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(trace_id)s: - %(levelname)s: %(message)s"))
handler.addFilter(RequestIDLogFilter())  # << Add request id contextual filter
logger.addHandler(handler)
log = logger

# DB class
app = Flask(__name__, template_folder=root_path + 'templates')
log.info(local_config.DB_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = local_config.DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


log.info('tuomatuo core init................................')