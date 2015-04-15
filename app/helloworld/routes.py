

def register_routes(blueprint):
    @blueprint.route('/helloworld')
    def hello_world():

        return "Hello World"
