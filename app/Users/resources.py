from flask.views import MethodView
from flask import Blueprint, request
from .models import Users

users_blueprint = Blueprint("users_blueprint", __name__, url_prefix="/api/")

class UsersList(MethodView):
    def get(self):
        return [{"name": "Luis"}, {"name": "Pedro"}]
    
    
class UsersResources(MethodView):
    def post(self):
        data = request.get.json()
        
        email = data.get('email')
        username = data.get('username')
        
        if email is None:
            return {"message": "No has ingresado tu email"}, 400
        if username is None:
            return {"message": "No has ingresado tu username"}, 400
        
        return {"Bienvenido"}
    
class UsersID(MethodView):
    def get(self, user_id):
        return 

users_blueprint.add_url_rule(
    "users",
    view_func=UsersList.as_view("users_list")
)

users_blueprint.add_url_rule(
    "users",
    view_func=UsersResources.as_view("users_resourses")
)

users_blueprint.add_url_rule(
    "users/<user_id>",
    view_func=Users.as_view("users_id")
)