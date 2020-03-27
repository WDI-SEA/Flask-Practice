from flask import Flask, jsonify
from flask import render_template
app=Flask(__name__)
name = 'Chris'
@app.route('/')
def hello():
	return 'Hello World'
@app.route('/greeting')
def greeting():
	return render_template('index.html',name=name)
ingredients = ['apple', 'pear', 'sugar']
@app.route('/pie')
def pie():
	return jsonify({'pie ingredients': ingredients})
