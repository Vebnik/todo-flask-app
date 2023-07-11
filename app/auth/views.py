from flask_restful import (
    Resource
)
from . import auth_api

from .serializers import UserSerializer
from .models import User


class ProfileApi(Resource):

    serializers = UserSerializer
    model = User

    def get(self):
        try:
            return {'ok': True, 'message': 'nice'}
        except Exception as ex:
            return {'ok': False, 'message': str(ex)}
    

auth_api.add_resource(ProfileApi, '/profile')

