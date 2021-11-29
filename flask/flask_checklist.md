# Get a Flask app up and running

## __ one off commands__
```
pip install pipenv
```

## __Steps__
1. Create a folder in which your curren assignment will live
2. Go into that folder
3. open terminal at verrent location
```
pipenv install PyMySQL flask
```
4. Create virtual env
    ```
    pipenv install flask
    ```
5. launch shell
    ```
    pipenv shell
    ```
    ```
    pipenv install flask-bcrypt
    ```
6. Create File Structure
    pipfile
    pipfile.lock
    templates
        index.html
    static
        css
            style.css
        js
            script.js
    server.py
7. Create server.py file
```py 
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

# Make sure this is at the bottom of your server.py file
if __name__=="__main__":
    app.run(debug=True)
