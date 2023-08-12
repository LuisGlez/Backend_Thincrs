from flask import Flask
from flask.views import MethodView
from .Users.resources import users_blueprint
from .Roles.resources import roles_blueprint
from .Categories.resources import categories_blueprint
from .Database import db
from flask_migrate import Migrate


class HelloWorld(MethodView):
    # Methods: POST, GET, PUT/PATCH, DELETE
    # C -> Create -> POST
    # R -> Read -> GET
    # U -> Update -> PUT / PATCH
    # D -> Delete -> DELETE
    def get(self): 
        return {'message': 'Hey there! Hello World :)'}
    
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config.from_pyfile('../settings.py')
    
    db.init_app(app)
    
    with app.app_context():
        migrate.init_app(app, db)
        
    hello_world = HelloWorld.as_view("hello_world")
    app.add_url_rule('/', view_func=hello_world)
    app.add_url_rule('/api/', view_func=hello_world)
    app.register_blueprint(users_blueprint)
    app.register_blueprint(roles_blueprint)
    app.register_blueprint(categories_blueprint)
    
    return app