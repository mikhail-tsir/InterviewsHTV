#delete elements in database

import pymongo
client = pymongo.MongoClient("mongodb+srv://Wen:1234[PASSWORD]@cluster0-gvhmp.mongodb.net/test?retryWrites=true&w=majority")
db = client["interview"]
col = db["users"]
col2 = db["storeData"]

def delUsers():
#deletes documents in users collection
    x = col.delete_many({})

#print(x.deleted_count, " documents deleted.")

#deletes documents in storeData collection
def delData():
    y = col2.delete_many({})
