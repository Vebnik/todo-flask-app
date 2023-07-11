from flask_restful import (
    Resource
)

from app import db
from . import todo_api
from .models import Todo
from .serializers import TodoSerializers


class TodoListApi(Resource):
    def get(self):
        try:
            todos = db.session.execute(db.select(Todo)).scalars().all()
            
            return {'ok': True, 'message': todos}, 200
        except Exception as ex:
            return {'ok': False, 'message': str(ex)}, 405


class TodoCreateApi(Resource):

    serializers = TodoSerializers()

    def post(self):
        try:
            data = self.serializers.get_data()

            return {'ok': True, 'message': data}, 201
        except Exception as ex:
            return {'ok': False, 'message': str(ex)}, 405


todo_api.add_resource(TodoListApi, '/list')
todo_api.add_resource(TodoCreateApi, '/create')