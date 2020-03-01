from flask import Response, request
from database.models import Tasks
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, TaskAlreadyExistsError, InternalServerError, UpdatingTaskError, DeletingTaskError, TaskNotExistsError

class TaskListAPI(Resource):
    def get(self):
        tasks = Tasks.objects().to_json()
        return Response(tasks, mimetype="application/json", status=200)

    def post(self):
        try:  
            body = request.get_json()
            task = Tasks(**body).save()
            id = task.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise TaskAlreadyExistsError
        except Exception as e:
            raise InternalServerError
 
class TaskAPI(Resource):
    def put(self, id):
        try:
            body = request.get_json()
            Tasks.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingTaskError
        except Exception:
            raise InternalServerError
 
    def delete(self, id):
        try:
            movie = Tasks.objects.get(id=id).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingTaskError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            tasks = Tasks.objects.get(id=id).to_json()
            return Response(tasks, mimetype="application/json", status=200)
        except DoesNotExist:
            raise TaskNotExistsError
        except Exception:
            raise InternalServerError


