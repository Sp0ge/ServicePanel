from flask import Flask, render_template
import configparser
from .routes.index import index_bp
import os
from .extentions import db, migrate, login

config = configparser.RawConfigParser()   
config.read("./config.conf")



app = Flask(__name__, static_folder='static/')
app.config['SECRET_KEY'] = "3aecf0fa3c22de921cba843775b268f2ca846a94"
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.get("postgres", "user")}:{config.get("postgres", "password")}@{config.get("postgres", "url")}:{config.get("postgres", "port")}/{config.get("postgres", "db")}' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)
login.init_app(app)

app.register_blueprint(index_bp)