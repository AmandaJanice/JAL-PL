from flask import Flask
import json

# app = Flask(__name__)
class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        self.action()
        return self.response

class Route_ID():
    def __init__(self, route, server_id):
        self.route = route
        self.server_id = server_id

class Server():

    def __init__(self, variables={}, port=80):
        self.app_port = port
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
        app = self.variables[server_id]

        #idea: make dict with routes/actions and run that
        #todo call all relevant functions base on given routes
        # app.add_url_rule('/', 'Home', lambda : 'Hello, World')
        app.add_url_rule(route_endpoint, str(route_endpoint), action)

        return

    def create_data(self, route_id, object_id):#PUT and POST
        ## TODO:
        object = self.variables[object_id]
        endpoint = self.variables[route_id]

        ## TODO: create action and call add_endpoints

        pass

    def read_data(self, route_id, object_id):#GET
        ## TODO:
        pass

    def create_server(self, assigned_id, port=80):
        self.variables[assigned_id] = Flask(assigned_id)
        self.app_port = port

    def start_server(self, server_id):
        self.variables[server_id].run(port=self.app_port)
