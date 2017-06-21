#!/usr/bin/env python

from flask import Flask
from flask import render_template, redirect, request, url_for, session as flask_session, jsonify

from flask_assets import Environment, Bundle
import dateparser
import datetime
import babel.dates
import numpy as np

from db import Session
from flask_sqlalchemy_session import flask_scoped_session
from sqlalchemy import func

from models import Band
import json


app = Flask(__name__,static_url_path='/static')
session = flask_scoped_session(Session, app)

import json
from flask import Flask,jsonify
app = Flask(__name__)



from functools import wraps
from flask import redirect, request, current_app

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data) + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function

# then in your view
#@default.route('/test', methods=['GET'])
#def test():
#    return jsonify({"foo":"bar"})

@app.route('/bands.json')
@support_jsonp
def bands():
    with open("bands.json") as f:
        bjson = json.load(f)
        
    return jsonify(bjson)




@app.route('/bandnames.json')
@support_jsonp
def bandnames():
    return jsonify([b.bandname for b in session.query(Band).all()])


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = "debug launcher")
    parser.add_argument('--debug', dest="debug", action="store_true")
    args = parser.parse_args()

    if args.debug:
        app.run( debug=True, host='0.0.0.0', port=5052)
    else:
        app.run( host='0.0.0.0', port=5052)
