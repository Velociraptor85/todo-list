import socket
from flask import Response, request
from flask_restful import Resource
from resources.errors import InternalServerError 

class Hostname(Resource):
    def get(self):
        try:
            return Response(socket.gethostname(), mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

class APIVersion(Resource):
    def get(self):
        try:
            return Response('v1.0', mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

class Uptime(Resource):
    def get(self):
        try:
            return Response('', mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError

class Running(Resource):
    def get(self):
        try:
            return Response('True', mimetype="application/json", status=200)
        except Exception:
            raise InternalServerError
