
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "Shhhhhhhh"                                                   

@app.route('/')                                                                  
def index():
    return render_template("index.html")


@app.route('/process', methods=['POST'])                                     
def process():
    session['fname'] = request.form['fname']
    session['lname'] = request.form['lname']
    session['location'] = request.form['location']
    session['fav_Language'] = request.form['fav_Language']
    session['comment'] = request.form['comment']
    return render_template("result.html")



if __name__=="__main__":   
    app.run(debug=True)    