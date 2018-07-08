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
	data = get_data()
	return render_template('index.html', data=data)

@app.route('/demo/')
def demo():
	return render_template('safe_index.html')

@app.route('/add_comment/', methods=['POST'])
def add_comment():
	# if record_comment(img_id, img_name, text, score=0, user="Unknown"):
	return "SUCCESS!"

@app.route('/posts/<img_id>/')
def info(img_id):
	return render_template('post.html')

@cross_origin()
@app.route('/add_image/<name>/<user>/<source>/<source_link>/')
def add_img(name, user, source, source_link):
	source_link = "https://"+source_link
	if record_img(name, user, source, source_link):
		return "SUCCESS!"



# HELPERS
def retrieve_imgs():
	imgs = []
	q = models.Img.query.all()
	for i, line in enumerate(q):
		imgs.append({"id":line.id, "name":line.name, 
					 "source": line.source, "source_link": line.source_link})
	return imgs

def retrieve_comments(ide, name):
	comms = []
	q = models.Comment.query.filter_by(img_id=ide)
	for i, line in enumerate(q):
		if line.img_id == ide and line.img_name == name:
			comms.append({"id": line.id, "user": line.username, "text": line.text, "score": line.score})

	comms = [comm for comm in sorted(comms, key=lambda x: x["score"], reverse=True)]
	return comms

def get_data():
	data = {}
	imgs = retrieve_imgs()
	for img in imgs:
		comments = retrieve_comments(img["id"], img["name"])
		data[img["id"]] = {"id": img["id"], "name": img["name"], "source": img["source"],
						   "source_link": img["source_link"], "comments": comments}

	return data

def record_comment(img_id, img_name, text, score=0, user="Unknown"):
	comment = models.Comment(text, user, score, img_id, img_name)
	db.session.add(comment)
	db.session.commit()
	return True

def record_img(name, user, source, source_link):
	img = models.Img(name, user, source, source_link)
	db.session.add(img)
	db.session.commit()
	return True

if __name__ == '__main__':
	# # Deploying
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # Debugging
    # app.run(debug=True, host='0.0.0.0')
