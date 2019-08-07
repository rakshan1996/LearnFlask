import os
from flask import Flask
from . import db
from . import auth



def create_app(test_config=None):
	#create and configure the app

	app= Flask(__name__,instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path,'flaskr.sqlite')
	)
	app.config["DEBUG"]=True

	if test_config is None:
		#Load the instance config,if it exists when not testing
		app.config.from_pyfile('config.py',silent=True)
	else:
		app.config.from_mapping(test_config)


	#ensure the instance folder exsists




	try: 
		os.makedirs(app.instance_path)
	except OSError:
		pass


	@app.route('/')
	def hello_world():
		return 'Hello Devil, Welcome to the world of Python.'

	db.init_app(app)
	app.register_blueprint(auth.bp)
	return app
