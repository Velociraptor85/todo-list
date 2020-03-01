import os
from flask import Flask
from flask_restful import Api
from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors


app = Flask(__name__)
api = Api(app, errors=errors)

app.config['MONGODB_DB'] = os.getenv('MONGODB_DATABASE', 'test')
app.config['MONGODB_HOST'] = os.getenv('MONGODB_HOST', 'localhost')
app.config['MONGODB_PORT'] = os.getenv('MONGODB_PORT', 27017)
app.config['MONGODB_USERNAME'] = os.getenv('MONGODB_USERNAME', '')
app.config['MONGODB_PASSWORD'] = os.getenv('MONGODB_PASSWORD', '')
#app.config['API_VERSION'] = 'v1.0'

#initialize Database
initialize_db(app)

#initialize API
initialize_routes(api)

#run Server
app.run()
