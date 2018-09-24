# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：      earth_map
   Description :
   Author :         xjk
   date：           2018/9/13
-------------------------------------------------
   Change Activity: 2018/9/13:
-------------------------------------------------
"""
from core import app, logger, db
from model.client import TransporterGeo
from utils.sys_decorator import aspect
from flask import render_template
__author__ = 'xujiankang'



@app.route("/map")
@aspect('')
def earth_map():
    return render_template("map.html", content="")


@app.route("/map/init")
@aspect('')
def earth_map_init():
    for line in open('/Users/xjk/Documents/pythonWorkSpace/tuomatuo/zongjie/geo.sql'):
        logger.info("**************line : %s", line);
        transporter_geo = TransporterGeo()
        transporter_geo.transporter_id = 3683190
        transporter_geo.lat = line.split(',')[1]
        transporter_geo.lng = line.split(',')[0]
        transporter_geo.time = line.split(',')[2]
        logger.info("*********** transporter_geo : %s", transporter_geo.to_dict())
        db.session.add(transporter_geo)
        db.session.commit()
    return 'OK'