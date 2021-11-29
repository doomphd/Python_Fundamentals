from werkzeug import datastructures
from flask_app import app
from flask import render_template, session, redirect, request
from flask_app.models import user
from flask import flash

from flask_bcrypt import Bcrypt                                         # we are creating an object called bcrypt, 
bcrypt = Bcrypt(app)                                                    #   which is made by invoking the function Bcrypt with our app as an argument 

@app.route('/')                                                         # Main Page
def root():
    print("******** in index *******************")
    if 'uuid' in session:                                              # check if user is logged in
        print("User is logged in, rerouting to dashboard")
        return redirect("/registration")
    return render_template("index.html")

@app.route('/logout')                                                   # Logout User
def logout():
    del session['uuid']
    return redirect("/")

# //// FORM POST /////////////////////////////////

@app.route('/registration/post', methods=['POST'])                      # Function that handles regisstration form data
def registration_post():
    print("**** In Registration POST ****")

    if not user.User.validate_user(request.form):    # If a login field is invalid, redirect to root
        return redirect('/')
    
    # **** Start hashing the password ********
    hash_pw = bcrypt.generate_password_hash(request.form['pw'])
                                           # Save the hashed pwd   
    data = {
        **request.form,
        'hash_pw': hash_pw
    }
    
    id = user.User.create(data)
    session['uuid'] = id

    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { 
        **request.form 
    }
    # user is not registered in the db
    if not user.User.validate_login(data):    # If a login field is invalid, redirect to root
        flash("Invalid Email/Password")
        return redirect("/")
    else:        
        user_in_db = user.User.get_by_email(data)
        print(user_in_db.first_name,user_in_db.last_name,user_in_db.email)
        session['uuid'] = user_in_db.id
    # if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
    #     # if we get False after checking the password
    #     flash("Invalid Email/Password")
    #     return redirect('/')
    # if the passwords matched, we set the user_id into session
    # never render on a post!!!
    return redirect("/registration")
# //// CREATE ////////////////////////////////////

@app.route('/registration')
def registration():
    if not 'uuid' in session:                                              # Check if user is logged in
        print("User is not logged in, redirect to root login")
        return redirect("/")                                                # If not logged in, redirect to root login
    data = {
        'id': session['uuid']
    }
    print("data:")
    print(data)
    #users = user.User.get_one(data)                             # Retrive user's info from db and make a user instance
    print("User:")
    
    return render_template("logged_in.html", )