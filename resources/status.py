import socket
from flask import Response, request
from flask_restful import Resource
from resources.errors import InternalServerError 

class Hostname(Resource):
    def get(self):
        try:
            return Response('{"hostname": "' + str(socket.gethostname()) + '"}', mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

class APIVersion(Resource):
    def get(self):
        try:
            return Response('{"api_version": "v1.0"}', mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

class Uptime(Resource):
    def get(self):
        try:
            return Response('{"uptime": ""}', mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

class Running(Resource):
    def get(self):
        try:
            return Response('{"running": true}', mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

class Index(Resource):
    def get(self):
        try:
            return Response('Welcome to this todo-list service.', status=200)
        except Exception:
            raise InternalServerError
