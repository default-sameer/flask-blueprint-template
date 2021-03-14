from flask import Flask
from .config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from .public.views import public
    app.register_blueprint(public)
    
    from .admin.views import admin
    app.register_blueprint(admin)
    
    return app
