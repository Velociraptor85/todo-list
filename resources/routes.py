from .movie import TaskListAPI, TaskAPI

def initialize_routes(api):
 api.add_resource(TaskListAPI, '/api/v1.0/todo')
 api.add_resource(TaskAPI, '/api/v1.0/todo/<id>')
