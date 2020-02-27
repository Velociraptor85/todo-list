import os
from flask import Flask
from database.db import initialize_db
from resources.routes import initialize_routes
from resources.errors import errors

app = Flask(__name__)
api = Api(app, errors=errors)

db_hostname = os.getenv('MONGODB_HOST', localhost)
db_name = os.getenv('MONGODB_DATABASE', mongodb)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://'.db_hostname.'/'.db_name
}

initialize_db(app)

initialize_routes(api)

app.run()
