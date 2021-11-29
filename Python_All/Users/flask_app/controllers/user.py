from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models import model_user

@app.route('/')
def index():
    return redirect('/users')
@app.route("/users")
def users():
    # call the get all classmethod to get all friends
    users = model_user.User.get_all()
    print(users)
    return render_template("index.html", users = users)

@app.route("/users/new")
def new():
    # call the get all classmethod to get all friends
    users = model_user.User.get_all()
    return render_template("new.html", users = users)

# @app.route("/users/show")
# def show():
#     # call the get all classmethod to get all friends
#     users = User.get_all()
#     return render_template("show.html", users = users)

@app.route("/users/<int:id>/edit")
def edit(id):
    # call the get all classmethod to get all friends
    data = {"id":id}
    return render_template("edit.html", user = model_user.User.get_one(data))

@app.route('/users/<int:id>')
def show(id):
    data = {"id":id}
    return render_template('show.html', user=model_user.User.get_one(data))
            
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # We pass the data dictionary into the save method from the Friend class.
    model_user.User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/users')

@app.route("/users/<int:id>/update", methods=["POST"])
def update_user(id):
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        **request.form,
        'id': id
    }
    # We pass the data dictionary into the save method from the Friend class.
    model_user.User.update(data)
    # Don't forget to redirect after saving to the database.
    return redirect(f'/users/{id}')


@app.route('/users/<int:id>/delete')
def delete(id):
    data = {'id':id}
    model_user.User.delete(data)
    return redirect('/users')
