from flask_app import app                                               # Import flask app
from flask_app.controllers import controller_user, controller_routes,controller_task                   # Import Controllers
if __name__ == "__main__":
    app.run(debug=True)