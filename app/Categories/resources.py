from flask.views import MethodView
from flask import Blueprint, request

categories_blueprint = Blueprint("categories_blueprint", __name__, url_prefix="/api/")

class CategoriesList(MethodView):
    def get(self):
        return [{"id": "1", "category name": "info"}, {"id": "2", "category name": "info"}], 200
    

class Categories(MethodView):
    def post(self):
        data = request.get_json()
        
        category_name = data.get("category name")
        
        if category_name is None:
            return {"mesage": "No ingresaste el nombre de la categoria"}, 400
        
        return {"Categoria agregada con exito"}, 201


class Category_id(MethodView):
    def get(self):
        data = request.get_json()
        
        category_id = data.get("id")
        
        if category_id is None:
            return {"message": "Categoria no valida"}, 400
        
        return {"Aqui va la info de la categoria seleccionada"}
    
categories_blueprint.add_url_rule(
    "categories",
    view_func=CategoriesList.as_view("categories_list")
)

categories_blueprint.add_url_rule(
    "categories",
    view_func=Categories.as_view("categories")
)

categories_blueprint.add_url_rule(
    "categories",
    view_func=Category_id.as_view("category_id")
)