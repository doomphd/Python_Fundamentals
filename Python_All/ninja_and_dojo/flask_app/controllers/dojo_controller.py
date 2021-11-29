from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models import ninja,dojo

@app.route('/')
def index():
    return redirect('/dojos')


@app.route("/dojos")
def users():
    dojos = dojo.Dojo.get_all()
    return render_template("index.html", dojos = dojos)

@app.route("/create")
def ninjas_create():
    dojos = dojo.Dojo.get_all()                             
    return render_template("new.html", dojos = dojos)

@app.route('/dojos/<int:id>')                                          
def dojos_id(id):
    data = {
        'id': id
    }
    dojos = dojo.Dojo.get_dojo_with_users(data)
    return render_template("show.html", dojos = dojos)



@app.route('/dojos/post', methods=['POST'])                             
def dojos_post():
    data = {                                                           
        'name': request.form['name'],
    }

    dojo.Dojo.create(data)                              
    return redirect("/dojos")

@app.route('/create_ninja', methods=['POST'])                     
def ninjas_create_post():
    data = {                                                           
        'dojo_id': request.form['dojo_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age']
    }

    ninja.Ninja.save(data)                          
    return redirect(f"/dojos/{ data['dojo_id'] }")