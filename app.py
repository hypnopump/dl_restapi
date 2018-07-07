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

app = Flask(__name__)
app.config.from_pyfile('utils/config.py')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from utils import models
db.create_all()

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def web():
	data = None
	# data = get_data()
	return render_template('index.html', data=data)

@app.route('/add_comment/', methods=['POST'])
def add_img():
	# if record_img(name, user):
	return "SUCCESS!"

@app.route('/posts/<img_id>/')
def info():
	return render_template('post.html')

@cross_origin()
@app.route('/add_img/<name>/<user>/')
def add_img():
	if record_img(name, user):
		return "SUCCESS!"



# HELPERS
def retrieve_imgs():
	imgs = []
	q = models.Img.query.all()
	for i, line in enumerate(q):
		imgs.append({"id":line.id, "name":line.name})
	return imgs

def retrieve_comments(id, name):
	comms = []
	q = models.Comment.query.all()
	for i, line in enumerate(q):
		if line.img_id == id and line.img_name == name:
			comms.append({"user": line.user, "text": line.text, "score": line.score})

	comms = [comm for comm in sorted(comms, key=lambda x: x["score"], reverse=True)]
	return comms

def get_data():
	data = {}
	imgs = retrieve_imgs()
	for img in imgs:
		comments = retrieve_comments(img["id"], img["name"])
		data[img["id"]] = {"id": img["id"], "name": img["name"], "comments": comments}

	return data

def record_comment(img_id, img_name, text, score=0, user="Unknown"):
	comment = models.Comment(text, user, score, img_id, img_name)
	db.session.add(comment)
	db.session.commit()
	return True

def record_img(name, user):
	img = models.Img(name, user)
	db.session.add(img)
	db.session.commit()
	return True

if __name__ == '__main__':
	# # Deploying
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # Debugging
    # app.run(debug=True, host='0.0.0.0')
