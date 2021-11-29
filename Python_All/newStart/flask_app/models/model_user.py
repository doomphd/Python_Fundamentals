# import the function that will return an instance of a connection ////////
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
from flask_app import DATABASE_SCHEMA

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

TABLENAME = "users"                                                     # Designates the table we are using

class User:
    def __init__( self , data ):                                        # Constructor function
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.hash_pw = data['hash_pw']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    # **** Insert One Method ***********************************************
    # @returns ID of created user
    @classmethod
    def create(cls, data):
        query = "INSERT INTO " + TABLENAME +" (first_name, last_name, email, hash_pw) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(hash_pw)s );"
        # data is a dictionary that will be passed into the save method from server.py
        new_users_id = connectToMySQL(DATABASE_SCHEMA).query_db( query, data )
        return new_users_id
        
    # //// RETRIEVE /////////////////////////////////////////////////////////

    # **** Get All Class Method *******************************************
    # @Returns: a list of instances of the class
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM " + TABLENAME + ";"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query)        # Call the connectToMySQL function with the target db
        users = []                                          # Initialize an empty list where we can store instances of the class
        for class_instance in results:                                  # Iterate over the db results and create instances of the cls objects
            users.append( cls(class_instance) )             # Add each instance of the class to the list of instances
        return users
    
    # **** Get One Class Method *******************************************
    # @Returns: an instance of the class
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM " + TABLENAME +" WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)  # Call the connectToMySQL function with the target db
                                                                        # result is a list of a single dictionary
        return cls(results[0])                                          # return an instance of the dictionary

    # **** Get One by Email Class Method **********************************
    # @Returns: an instance of the class
    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM " + TABLENAME +" WHERE email = %(email)s;"
        results = connectToMySQL(DATABASE_SCHEMA).query_db(query, data)  # Call the connectToMySQL function with the target db
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
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

    # //// DELETE //////////////////////////////////////////////////////////

    # **** Delete One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM " + TABLENAME + " WHERE id=%(id)s"
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

    @staticmethod
    def validate_users(data):
        is_valid = True

        if len(data['first_name']) < 1:
            is_valid = False
            flash('first_name name is required', 'err_reg_first_name')

        if len(data['last_name']) < 1:
            is_valid = False
            flash('last_name name is required', 'err_reg_last_name')

        if len(data['email']) < 1:
            is_valid = False
            flash('email email is required', 'err_reg_email')

        if len(data['pw']) < 1:
            is_valid = False
            flash('pw pw is required', 'err_reg_pw')

        if len(data['confirm_pw']) < 1:
            is_valid = False
            flash('confirm_pw name is required', 'err_reg_confirm_pw')

        if(data['confirm_pw'] != data['pw']):
            is_valid = False
            flash('Passwords do not match', 'err_reg_confirm_pw')

        return is_valid

    @staticmethod
    def validate_users_login(data):
        is_valid = True

        if len(data['email']) < 1:
            is_valid = False
            flash('email email is required', 'err_login_email')

        else:
            potential_user = User.get_one_by_email({'email': data['email'] })
            if not potential_user:
                is_valid = False
                flash('email not found', 'err_login_email')

        if len(data['pw']) < 1:
            is_valid = False
            flash('pw pw is required', 'err_login_pw')


        return is_valid