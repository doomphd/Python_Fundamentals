from flask import Flask, render_template  

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/play')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template("index.html",num=3,color="aqua")



@app.route('/play/<int:num>')
def say(num):
    return render_template('index.html', times=num, color ="aqua")
@app.route('/play/<int:num>/<string:color>')
def repeat(num, color):
    return render_template('index.html', times=num, color = color)

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! no response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

