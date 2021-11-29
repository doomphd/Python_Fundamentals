# import the function that will return an instance of a connection ////////
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
from flask_app import app                                               # import app for use in bcrypt
from flask_bcrypt import Bcrypt                                         # we are creating an object called bcrypt, 
bcrypt = Bcrypt(app)                                                    #   which is made by invoking the function Bcrypt with our app as an argument

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

TARGETDATABASE = 'login/registration'                              # Designates the database we are using
TABLENAME = "users"                                                     # Designates the table we are using

class User:
    def __init__( self , data ):                                        # Constructor function
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.hash_pw = data['hash_pw']



    @staticmethod
    def validate_user(data):
        is_valid = True
        # //// Validate User First Name ///////
        if len(data['first_name']) < 2:
            flash("First Name must be at least 2 characters in length","error_login_user_first_name")
            is_valid = False
        elif not data['first_name'].isalpha():
            flash("First Name must be letters only","error_login_user_first_name")
            is_valid = False

        # //// Validate User Last Name ////////
        if len(data['last_name']) < 2:
            flash("Last Name must be at least 2 characters in length","error_login_user_last_name")
            is_valid = False
        elif not data['last_name'].isalpha():
            flash("Last Name must be letters only","error_login_user_last_name")
            is_valid = False

        # //// Validate User Email ////////
        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address", "error_login_user_email")
            is_valid = False
        # elif User.get_by_email(data):
        #     flash("Invalid email already registered", "error_login_user_email")
        #     is_valid = False
        
        # //// Validate Password ////////
        if len(data['pw']) < 8:
            flash("Password must be at least 8 characters in length", "error_login_user_password")
            is_valid = False
        
        # //// Validate Confirm Password ////////
        if data['pw'] != data['confirm_password']:
            flash("Password and Confirm Password do not match", "error_login_user_confirm_password")
            is_valid = False

        return is_valid

        # **** Function to Validate Login User Data from Login Form ********
    @staticmethod
    def validate_login(data):
        is_valid = True
        login_user = User.get_by_email(data)
        

        # //// Validate User Email ////////
        if not EMAIL_REGEX.match(data['email']):                                # Check if email format is valid
            flash("Invalid email address", "error_login_user_login_email")
            is_valid = False
        elif not login_user:                                                    # check if email is registered in db
            flash("Email has not yet been registered", "error_login_user_login_email")
            is_valid = False
    
        # //// Validate Password ////////
        if len(data['pw']) < 8:
            flash("Password must be at least 8 characters in length", "error_login_user_login_password")
            is_valid = False
        
        if is_valid:
            if not bcrypt.check_password_hash(login_user.hash_pw, data['pw']):
                flash("Invalid Email Password Combination", "error_login_user_login_password")
                is_valid = False
        
        return is_valid

    # # **** Function to generate password hash ********
    # @staticmethod
    # def generate_password_hash(pw):
    #     return bcrypt.generate_password_hash(pw)
    # //// CREATE //////////////////////////////////////////////////////////

    # **** Insert One Method ***********************************************
    # @returns ID of created user
    @classmethod
    def create(cls, data):
        query = "INSERT INTO " + TABLENAME +" (first_name, last_name, email, hash_pw) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(hash_pw)s );"
        # data is a dictionary that will be passed into the save method from server.py
        new_users_id = connectToMySQL(TARGETDATABASE).query_db( query, data )
        return new_users_id
        
    # //// RETRIEVE /////////////////////////////////////////////////////////

    # **** Get All Class Method *******************************************
    # @Returns: a list of instances of the class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM " + TABLENAME + ";"
        results = connectToMySQL(TARGETDATABASE).query_db(query)        # Call the connectToMySQL function with the target db
        users = []                                          # Initialize an empty list where we can store instances of the class
        for class_instance in results:                                  # Iterate over the db results and create instances of the cls objects
            users.append( cls(class_instance) )             # Add each instance of the class to the list of instances
        return users
    
    # **** Get One Class Method *******************************************
    # @Returns: an instance of the class
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM " + TABLENAME +" WHERE id = %(id)s;"
        results = connectToMySQL(TARGETDATABASE).query_db(query, data)  # Call the connectToMySQL function with the target db
                                                                        # result is a list of a single dictionary
        return cls(results[0])                                          # return an instance of the dictionary

    # **** Get One by Email Class Method **********************************
    # @Returns: an instance of the class
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM " + TABLENAME +" WHERE email = %(email)s;"
        results = connectToMySQL(TARGETDATABASE).query_db(query, data)  # Call the connectToMySQL function with the target db
                                                                        # result is a list of a single dictionary
        if len(results) == 0:
            return False
        return cls(results[0])                                          # return an instance of the dictionary

    # //// UPDATE //////////////////////////////////////////////////////////

    # **** Update One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def update_one(cls, data):
        query = "UPDATE " + TABLENAME +" SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, password=%(password)s WHERE id=%(id)s"
        return connectToMySQL(TARGETDATABASE).query_db(query, data)

    # //// DELETE //////////////////////////////////////////////////////////

    # **** Delete One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM " + TABLENAME + " WHERE id=%(id)s"
        return connectToMySQL(TARGETDATABASE).query_db(query, data)