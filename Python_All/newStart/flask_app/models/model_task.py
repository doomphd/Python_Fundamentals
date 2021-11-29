# import the function that will return an instance of a connection ////////
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re	# the regex module
from flask_app import DATABASE_SCHEMA
from flask_app.models import model_user

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

TABLENAME = "tasks"                                                     # Designates the table we are using

class Task:
    def __init__( self , data ):                                        # Constructor function
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.due_date = data['due_date']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @property
    def creator(self):
        return model_user.User.get_one({'id': self.user_id})
        

    # **** Insert One Method ***********************************************
    # @returns ID of created user
    @classmethod
    def create(cls, data):
        query = "INSERT INTO " + TABLENAME +" (name, description, due_date, user_id) VALUES ( %(name)s, %(description)s, %(due_date)s, %(user_id)s );"
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



    # //// UPDATE //////////////////////////////////////////////////////////

    # **** Update One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def update_one(cls, data):
        query = "UPDATE " + TABLENAME +" SET name=%(name)s, description=%(description)s, due_date=%(due_date)s WHERE id=%(id)s"
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

    # //// DELETE //////////////////////////////////////////////////////////

    # **** Delete One Class Method *****************************************
    # @Returns: Nothing
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM " + TABLENAME + " WHERE id=%(id)s"
        return connectToMySQL(DATABASE_SCHEMA).query_db(query, data)

    @staticmethod
    def validate_tasks(data):
        is_valid = True

        if len(data['name']) < 1:
            is_valid = False
            flash('task name is required', 'err_reg_name')

        if len(data['description']) < 1:
            is_valid = False
            flash('description is required', 'err_reg_description')

        if len(data['due_date']) < 1:
            is_valid = False
            flash('due date is required', 'err_reg_due_date')

 

        return is_valid
