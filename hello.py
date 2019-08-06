from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello Devil, Welcome to the world of Python.'

@app.route('/routesCheck/')
def route_check():
		return "route"

@app.route('/about')
def about():
		return "testComplete"