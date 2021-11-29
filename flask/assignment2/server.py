from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/page2/<name>')
def page2(name):
    print(name)
    return render_template('page2.html')
@app.route('/page3')
def page3():
    print(session['email'])
    print(session['pw'])
    return render_template('page3.html')


@app.route('/page3_process', methods = ['POST'])
def page3_process():
    print(request.form)
    session['email']= request.form['email']
    session['pw']= request.form['pw']

    return redirect('page3.html')

if __name__=="__main__":
    app.run(debug=True)

some_dict = {
    'key':'values'
}