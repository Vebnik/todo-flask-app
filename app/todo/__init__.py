from flask import (
    Blueprint, 
)
from flask_restful import (
    Api
)

todo = Blueprint('todo', __name__, url_prefix='/api/todo')
todo_api = Api(todo)


from . import views
from . import models