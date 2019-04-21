from flask import Flask
from flask import request
import json

class Route_ID():
    def __init__(self, route, server_id):
        self.route = route
        self.server_id = server_id

class Server_ID():
    def __init__(self, flask_instance, port):
        self.flask_instance = flask_instance
        self.port = port

class Server():

    def __init__(self, variables={}):
        self.variables = variables #parser stores id's to this dict

    def update_variables(self, var_id, object):
        parsed = json.loads(object)

        #check if values in variables and replaces them with appropriate variables
        for key in parsed:
            if parsed[key] in self.variables:
                parsed[key] = self.variables[parsed[key]]

        self.variables[var_id] = parsed

    def add_route(self, route_id, server_id, route):
        self.variables[route_id] = Route_ID(route, server_id)

    def add_endpoints(self, server_id, route_endpoint, action):
        app = self.variables[server_id].flask_instance

        # app.add_url_rule('/', 'Home', lambda : 'Hello, World')

        app.add_url_rule(route_endpoint, str(route_endpoint), action)

        return

    def create_data(self, route_id, object_id):#TODO PUT and POST
        object = self.variables[object_id]
        endpoint = self.variables[route_id]

        def create_action():
            object = request.get_json()
            return str(object)

        self.add_endpoints(endpoint.server_id, endpoint.route, create_action)

    def read_data(self, route_id, object_id):#TODO GET
        ## TODO:
        object = self.variables[object_id]
        endpoint = self.variables[route_id]

        def return_action():
            return str(object)

        self.add_endpoints(endpoint.server_id, endpoint.route, return_action)

    def create_server(self, assigned_id, port=80):
        self.variables[assigned_id] = Server_ID(Flask(assigned_id), port)

    def start_server(self, server_id):
        self.variables[server_id].flask_instance.run(port=self.variables[server_id].port)
