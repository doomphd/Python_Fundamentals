from flask_app import app, bcrypt
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_task,model_user


@app.route('/task/new')
def new_task():
    context = {
        'user': model_user.User.get_one({'id': session['uuid']})
    }
    return render_template('task.html', **context)

@app.route('/task/create', methods = ['post'])
def create_task():
    is_valid = model_task.Task.validate_tasks(request.form)

    if not is_valid:
        return redirect('/task/new')
    
    data = {
        **request.form,
        'user_id':session['uuid']
    }
    model_task.Task.create(data)
    return redirect ('/')

@app.route('/task/<int:id>')
def show_task(id):
    context = {
        'user': model_user.User.get_one({'id': session['uuid']}),
        'task': model_task.Task.get_one({'id': id})
    }
    return render_template('show.html', **context)

@app.route('/task/<int:id>/edit')
def edit_task(id):
    context = {
        'user': model_user.User.get_one({'id': session['uuid']}),
        'task': model_task.Task.get_one({'id': id})
    }

    return render_template('edit.html', **context)

@app.route('/task/<int:id>/update', methods=['post'])
def update_task(id):
    is_valid = model_task.Task.validate_tasks(request.form)

    if not is_valid:
        return redirect(f'/task/{id}/edit')

    data = {
        **request.form,
        'id':id
    }
    
    model_task.Task.update_one(data)
    return redirect('/')

@app.route('/task/<int:id>/delete')
def delete_task(id):
    model_user.User.delete({{'id':id}})

    return redirect('/')