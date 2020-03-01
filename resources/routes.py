from .task import TaskListAPI, TaskAPI
from .status import APIVersion, Uptime, Hostname, Running

def initialize_routes(api):
 api.add_resource(TaskListAPI, '/api/v1.0/todo/list')
 api.add_resource(TaskAPI, '/api/v1.0/todo/<id>')
 api.add_resource(APIVersion, '/api/status/version')
 api.add_resource(Running, '/api/status/running')
 api.add_resource(Uptime, '/api/status/uptime')
 api.add_resource(Hostname, '/api/status/hostname')
