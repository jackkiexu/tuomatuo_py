# -*- encoding: utf8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, String, Date, Float
from config import local_config
from logzero import logger
import logzero

# log_format = '%(color)s[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d]%(end_color)s %(message)s'
# formatter = logzero.LogFormatter(fmt=log_format)
# logzero.setup_default_logger(formatter=formatter)
log = logger

# DB class
app = Flask(__name__)
logger.info(local_config.DB_URI)
app.config['SQLALCHEMY_DATABASE_URI'] = local_config.DB_URI
db = SQLAlchemy(app)


log.info('tuomatuo core init................................')