
from .models import User

class UserSerializer:
    def __init__(self, model: User) -> None:
        self.model = model

    def data(self):
        return {
            'name': 'self.model.name',
        }
    