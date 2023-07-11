from flask import (
    Blueprint, 
)
from flask_restful import (
    Api
)

auth = Blueprint('auth', __name__, url_prefix='/api/auth')
auth_api = Api(auth)


from . import views
from . import models