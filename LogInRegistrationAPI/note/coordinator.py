from pymongo import MongoClient

class Note_Coordinator():

    def __init__(self):
        '''Here it'll connect the database by using pymongo'''
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['Userregistration']
        self.collection=self.db['Notes']

    def get_notes(self,data):
        '''This function will get notes according to the user_id'''
        all_data=[]
        user_id=data.get('user_id')
        note_data=self.collection.find({'user_id':user_id},{"_id":0})
        for datas in note_data:
            all_data.append(datas)
        return all_data    

    def post_notes(self,data):
        '''This method will get data from server and insert in collection'''
        title=data.get('title')
        description=data.get('description')
        user_id=data.get('user_id')
        prev_note_id=self.collection.find({},{'note_id':1,'_id':0}).sort('_id',-1).limit(1)
        new_note=prev_note_id[0]['note_id']
        inserted_data= self.collection.insert({'title':title,'description':description,'user_id':user_id,'note_id':new_note+1})
        return True

    def put_data(self,data):
        '''This function will get data from server and update the collection'''
        user_id=data.get('user_id')
        title=data.get('title')
        description=data.get('description')
        update_data=self.collection.update({'user_id':user_id},{'title':title,'description':description})
        return True

    def delete_data(self,data):
        '''This function will delete the note according to the User_id'''
        user_id=data.get('user_id')
        delete_all=self.collection.delete_many({'user_id':user_id})
        return True
    
