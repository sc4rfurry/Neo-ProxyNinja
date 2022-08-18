#!/usr/bin/python3
from flask import Flask
import secrets
from flaskext.markdown import Markdown



def generate_sec_key(length):
    return secrets.token_hex(length)

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SECRET_KEY"] = generate_sec_key(32)
    Markdown(app)
    
    
    from .views import views_route


    app.register_blueprint(views_route, url_prefix="/")
    
        
    return app

