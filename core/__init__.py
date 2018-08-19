# -*- encoding: utf8 -*-
import flask
from flask import Flask, request, g, current_app
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
from config import local_config
import logging
import uuid
from threading import local

thread_local = local()


def request_id():
    v = getattr(thread_local, 'request_id', None)
    if v is not None and v != '':
        return v
    original_request_id = ''
    if flask.has_request_context() :
        original_request_id = request.headers.get('request_id', '').strip()
    if original_request_id  == '':
        original_request_id = uuid.uuid4()
    setattr(thread_local, 'request_id', original_request_id)
    return original_request_id


class RequestIDLogFilter(logging.Filter):
    def filter(self, record):
        record.trace_id = request_id()
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
app = Flask(__name__)
log.info(local_config.DB_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = local_config.DB_URI
db = SQLAlchemy(app)


log.info('tuomatuo core init................................')