from pymongo import MongoClient
from datetime import datetime

class Coordinator():
    
    def __init__(self):
        '''Here it'll connect the database by using pymongo'''
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['Userregistration']
        self.collection=self.db['auth_user']

    def post_data(self,data):
        '''This function will check whether the username exists or not'''
        username=data.get('username')
        checked_data=self.collection.find({'username':username}).count()
        return checked_data,username

    def post_insert_data(self,data):
        '''This function will get data from server and then insert into table.
            Return: email and user_id'''
        username=data.get('username')
        password=data.get('password')
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        email=data.get('email')
        is_staff=0
        is_active=1
        is_superuser=0
        inserted_data=self.collection.insert({'first_name':first_name,'last_name':last_name,'email':email,'username':username,'password':password,'is_staff':is_staff,'is_active':is_active,'is_superuser':is_superuser,'date_joined':datetime.now()})
        user_id_data= self.collection.find_one({'username':username},{'_id':1})
        user_id=user_id_data['_id']
        return email,user_id

    def post_login_data(self,username):
        ''' This function will get the user_id and return it'''

        user_authentication= self.collection.find_one({'username':username},{'username':1,'password':1,'_id':0})
        return user_authentication

    def get_verify_email(self,user_id,username):
        ''' this function will check the id and username then return the whole data'''
        data=self.collection.find_one({'_id':user_id,'username':username},{'_id':1,'username':1})
        return data
