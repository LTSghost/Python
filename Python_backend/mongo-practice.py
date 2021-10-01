#pip install pymongo[srv]  安裝 Python 連接 MongoDB 套件    !!!要從powershell去安裝pymongo

#引入 pymongo 套件
import pymongo  
from bson.objectid import ObjectId

#連線到 MongoDB 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://LTSghost:limitless123@cluster0.cg02o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.website #選擇操作 website 資料庫
collection = db.members #選擇操作 members 集合

# result = collection.insert_many([{   # insert_many 新增多筆資料
#     'name':'LTS',
#     'passward':'limitless'
# },{
#     'name':'howard',
#     'passward':'drawssap'
# }]
# )

#把資料新增至集合 json格式   
# result_solo = collection.insert_one({            # insert_one 新增單筆資料  
#     "name":"LTS",
#     "gender":"male",
#     "love champion":"Varus"
# })

find_1 = collection.find_one(ObjectId("6155ab24aab7f450c9764adc"))  # find_one 取得單筆資料  引入bson套件 可用 ObjectId 指定要找的資料



Update_more_name = collection.update_many({
    'name':'LTSghost'
},{
    '$set':{
        'game':'League of Legneds'
    }
})

collection.update_one({
    'name':'howard'
},{
    '$set':{
        'game':'League of Legneds'   
    }
})

find_all = collection.find()
for doc in find_all:
    print(doc['game'])

print("Data added successfully")
# print(result.inserted_ids)
# print(result_solo.inserted_id)
print(find_1['name'])
print("Meet the criteria count",Update_more_name.matched_count)
print("Actual modification count",Update_more_name.modified_count)