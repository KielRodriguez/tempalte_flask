from flask import Flask

from .config import DevelopmentConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    from .usuarios import usuarios
    app.register_blueprint(usuarios)
    
    return app