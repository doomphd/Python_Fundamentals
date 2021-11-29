from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhhh"

DATABASE_SCHEMA = 'recipe_db'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)