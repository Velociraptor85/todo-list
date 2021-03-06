import os
from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors


app = Flask(__name__)
api = Api(app, errors=errors)

app.config['MONGODB_DB'] = os.getenv('MONGODB_DATABASE', 'sampledb')
app.config['MONGODB_HOST'] = os.getenv('MONGODB_HOST', 'localhost')
app.config['MONGODB_USERNAME'] = os.getenv('MONGODB_USER', '')
app.config['MONGODB_PASSWORD'] = os.getenv('MONGODB_PASSWORD', '')
#app.config['API_VERSION'] = 'v1.0'
APP_PORT=os.getenv('APPLICATION_PORT', '5000')

#initialize Database
initialize_db(app)

#initialize API
initialize_routes(api)

#run Server
#app.run()
app.run(host='0.0.0.0',port=APP_PORT)
