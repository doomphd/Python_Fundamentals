from flask import Flask, render_template  

app = Flask(__name__)    # Create a new instance of the Flask class called "app"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def home():
    return render_template("index.html",num=8, times = 8,color="red", color2= "black")



@app.route('/<int:y>')
def first(y):
    return render_template('index.html', num=y, times=8, color ="red", color2= "black")
@app.route('/<int:y>/<int:x>')
def second(y,x):
    return render_template('index.html', num=y, times=x, color ="red", color2= "black")

@app.route('/<int:y>/<int:x>/<string:color>')
def second(y,x,color):
    return render_template('index.html', num=y, times=x, color =color, color2= "beige")

@app.route('/<int:y>/<int:x>/<string:color>/<string:color>')
def second(y,x,color3):
    return render_template('index.html', num=y, times=x, color =color3, color2= "beige")


@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! no response. Try again."

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

