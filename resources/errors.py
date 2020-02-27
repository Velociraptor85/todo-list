class InternalServerError(Exception):
    pass

class SchemaValidationError(Exception):
    pass

class TaskAlreadyExistsError(Exception):
    pass

class UpdatingTaskError(Exception):
    pass

class DeletingTaskError(Exception):
    pass

class TaskNotExistsError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     "SchemaValidationError": {
         "message": "Request is missing required fields",
         "status": 400
     },
     "TaskAlreadyExistsError": {
         "message": "Task with given title already exists",
         "status": 400
     },
     "UpdatingTaskError": {
         "message": "Updating task added by other is forbidden",
         "status": 403
     },
     "DeletingTaskError": {
         "message": "Deleting task added by other is forbidden",
         "status": 403
     },
     "TaskNotExistsError": {
         "message": "Task with given id doesn't exists",
         "status": 400
     }
}
