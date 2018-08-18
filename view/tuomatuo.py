# -*- encoding: utf-8 -*-

from flask import Flask
from flask_zipkin import Zipkin
from py_zipkin.zipkin import zipkin_span
import requests
from py_zipkin.transport import BaseTransportHandler
import requests
from flask import Flask, request
from py_zipkin.zipkin import zipkin_span,create_http_headers_for_new_span
import time
from core.date_utils import my_date
from core import app, db, log


@zipkin_span(service_name='webapp', span_name='do_stuff')
def do_stuff():
    # time.sleep(2)
    headers = create_http_headers_for_new_span()
    r = requests.get('http://www.baidu.com', headers=headers)
    log.info(r)
    log.info(r.content)
    return 'OK'


def http_transport(encoded_span):
    # encoding prefix explained in https://github.com/Yelp/py_zipkin#transport
    #body = b"\x0c\x00\x00\x00\x01"+encoded_span
    body=encoded_span
    zipkin_url="http://127.0.0.1:9411/api/v2/spans"
    zipkin_url = "http://{host}:{port}/api/v2/spans".format(
       host=app.config["ZIPKIN_HOST"], port=app.config["ZIPKIN_PORT"])
    headers = {"Content-Type": "application/x-thrift"}
    r=requests.post(zipkin_url, data=body, headers=headers)
    log.info(type(encoded_span))
    log.info(encoded_span)
    log.info(body)
    log.info(r)
    log.info(r.content)


zipkin = Zipkin(sample_rate=10)
zipkin.init_app(app)


class HttpTransport(BaseTransportHandler):

    def get_max_payload_bytes(self):
        return None

    def send(self, payload):
        # The collector expects a thrift-encoded list of spans
        requests.post(
            'http://23.89.158.3:9411/api/v2/spans',
            data=payload,
            headers = {'Content-Type': 'application/x-thrift'},
        )


@app.route('/jack1')
def jack():
    log.info(request.data)
    return 'jack'


@app.route('/hello1')
def test():
    try:
        with zipkin_span(
            service_name='webapp',
            span_name='index',
            transport_handler=http_transport,
            port=5000,
            sample_rate=100,
        ):
            do_stuff()
            # time.sleep(1)
        log.info( '******************************************************')
    except Exception as ex:
        log.info( '******************************************************')
        log.error(ex)
        pass

    return "hello"


@app.route('/')
def hello_world():
    headers = {}
    headers.update(zipkin.create_http_headers_for_new_span())
    try:
        r = requests.get('http://www.baidu.com', headers= headers)
    except Exception as ex:
        log.error(ex)
        pass
    return r.text

