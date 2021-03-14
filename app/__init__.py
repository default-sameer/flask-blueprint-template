from flask import Flask

from .public.views import public
from .admin.views import admin

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(public)
    app.register_blueprint(admin)
    
    return app