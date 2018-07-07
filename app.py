#-*- coding: utf-8 -*-
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def web():
	return render_template('index.html')

# @app.route('/contact/')
# def contact():
# 	return render_template('contact.html')

# @app.route('/info/')
# def info():
# 	return render_template('info.html')

# @app.route('/register/')
# def register():
# 	return render_template('register.html')

# @app.route('/login/')
# def login():
# 	return render_template('login.html')

# @app.route('/in/')
# def in_():
# 	return render_template('in.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
