

class BaseConfig:
    SECRET_KEY = 'A SUPER PUPER SECRET KEY'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test_data.db'

