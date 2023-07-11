from flask_restful import (
    reqparse
)


class TodoSerializers:

    todo_parser = reqparse.RequestParser()

    def __init__(self) -> None:
        self.todo_parser.add_argument('text')
        self.todo_parser.add_argument('is_completed')
    
    def get_data(self):
        return self.todo_parser.parse_args()
