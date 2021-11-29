from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_user

@app.route('/logout')
def logout():
    del session['uuid']
    return redirect('/')

@app.route('/user/process_login', methods = ['post'])
def process_login():
    is_valid = model_user.User.validate_users_login(request.form)

    if not is_valid:
        return redirect('/')

    user = model_user.User.get_one_by_email({'email': request.form['email']})
    if not bcrypt.check_password_hash(user.hash_pw, request.form['pw']):
        flash('Invalid Credentials', 'err_login_pw')
        return redirect('/')
    
    session['uuid'] = user.id
    return redirect('/')


@app.route('/user/create', methods = ['post'])
def create_user():
    is_valid = model_user.User.validate_users(request.form)

    if not is_valid:
        return redirect('/')

    hash_pw = bcrypt.generate_password_hash(request.form['pw'])

    data = {
        **request.form,
        'hash_pw': hash_pw
    }
    id = model_user.User.create(data)
    session['uuid'] = id
    return redirect ('/')

@app.route('/user/<int:id>')
def show_user(id):
    return 'show_user'

@app.route('/user/<int:id>/edit')
def edit_user(id):
    return 'edit_user'

@app.route('/user/<int:id>/update', methods=['post'])
def update_user(id):
    return 'update_user'

@app.route('/user/<int:id>/delete')
def delete_user(id):
    return 'delete user'
