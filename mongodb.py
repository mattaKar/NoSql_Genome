# Install MongoDB:
# brew tap mongodb/brew
# brew install mongodb-community

import pymongo
import subprocess

subprocess.run(["brew","services","start","mongodb-community@4.2"])

myclient = pymongo.MongoClient('localhost', 27017)
db = myclient.db
col = db.mycollection
post = {"author": "Mike","text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"]}
post_id = col.insert_one(post).inserted_id
post_id

print(myclient.list_database_names())
print(db.list_collection_names())

cursor = col.find({})
for document in cursor:
    print(document)
