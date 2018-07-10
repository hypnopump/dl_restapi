#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request

# -*- coding: iso-8859-15 -
from flask_cors import CORS, cross_origin
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
import json
import hashlib

app = Flask(__name__)

@app.route('/')
def web():
	data = []
	return render_template('index.html', data=data)

@app.route('/demo/')
def demo():
	return render_template('safe_index.html')

@app.route('/post<id>/')
def post(id):
	return render_template('post.html')

@app.route('/leaderboard/')
def leader():
	return render_template('leader.html')

@app.route('/login/')
def login():
	return render_template('login.html')

@app.route('/signup/')
def signup():
	return render_template('signup.html', mess=None)

@app.route('/new_user/', methods = ['GET', 'POST'])
def new_user():
	username = request.form['username']
	email = request.form['email']
	password = hashlib.sha256(bytearray(request.form['password'], "utf-8")).hexdigest()
	re_password = hashlib.sha256(bytearray(request.form['re_password'], "utf-8")).hexdigest()

	if password != re_password:
		return render_template('signup.html', mess="Passwords don't match")

	return "Data received "+username+" / "+email+" / "+password+" / "+re_password


if __name__ == '__main__':
	# # Deploying
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)
    # Debugging
    app.run(debug=True, host='0.0.0.0')
