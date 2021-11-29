from flask import Flask
app = Flask(__name__)
app.secret_key = "shhhhhhh"

DATABASE_SCHEMA = 'nov_todo_db'

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)