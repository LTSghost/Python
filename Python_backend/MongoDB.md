**MongoDB 儲存資料的方式**

三層式的結構

．資料庫　Database

．集合   Collection

．文件   Document


![File](file.png)


MongoDB.com 


``` python

collection.insert_one({})

collection.insert_many([{,}])

collection.delete_one({})

collection.delete_many({})

collection.find_one(Objected()) # must from bson.objectid import ObjectId

find_all = collection.find()          # must all data have common 'key'
for doc in find_all:
	print(doc['key'])

collection.find_one({  # compound condition
    '$and/or':[
        {},{}
    ]
})

find_condition = collection.find({},sort = [
    ('key',pymongo.ASCENDING/DESCENDING)
])
for doc in find_condition:
    print(doc)

collection.update_one({},{"$set":{}})

collection.update_many({},{"$set":{}})

collection.update_one({},{"$unset":{}})

collection.update_one({},{"$inc":{}})

collection.update_one({},{"$mul":{}})

print("Actual deleted count",var.deleted_count)
print("Meet the criteria count",var.matched_count)
print("Actual modified count",var.modified_count)

```