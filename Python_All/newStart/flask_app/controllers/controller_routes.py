from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import model_user, model_task

@app.route('/')
def index():
    if 'uuid' in session:
        return redirect('/dashboard')
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    if 'uuid' not in session: 
        return redirect('/')
    context = {
        'user': model_user.User.get_one({'id': session['uuid']}),
        'all_tasks': model_task.Task.get_all()
    }
    return render_template('dashboard.html', **context)

@app.route('/', defaults = {'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'page not found'