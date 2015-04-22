from app.helloworld import views

def register_routes(blueprint):
    @blueprint.route('/helloworld')
    def hello_world():

        return views.Hello().render()
