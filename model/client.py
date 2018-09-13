# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      User
   Description :
   Author :         xjk
   date：           2018/9/6
-------------------------------------------------
   Change Activity: 2018/9/6:
-------------------------------------------------
"""
__author__ = 'xujiankang'

from core import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(32), nullable=False, unique=False, server_default='', index=True)
    role_id = db.Column(db.Integer, nullable=False, server_default='0')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


class TransporterGeo(db.Model):
    __tablename__ = 'transporter_geo'
    id = db.Column(db.BigInteger, nullable=False, primary_key=True, autoincrement=True)
    transporter_id = db.Column(db.BigInteger, nullable=False, server_default='0')
    lat = db.Column(db.DECIMAL, nullable=False, server_default='')
    lng = db.Column(db.DECIMAL, nullable=False, server_default='')
    time = db.Column(db.BigInteger, nullable=False, server_default='')

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
