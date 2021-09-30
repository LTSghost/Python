#pip install pymongo[srv]  安裝 Python 連接 MongoDB 套件    !!!要從powershell去安裝pymongo

import pymongo  #引入 pymongo 套件

#連線到 MongoDB 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://LTSghost:limitless123@cluster0.cg02o.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.website #選擇操作 website 資料庫
collection = db.members #選擇操作 members 集合

result = collection.insert_many([{   # insert_many 新增多筆資料
    'name':'LTS',
    'passward':'limitless'
},{
    'name':'howard',
    'passward':'drawssap'
}]
)

#把資料新增至集合 json格式   
result_solo = collection.insert_one({            # insert_one 新增單筆資料  
    "name":"LTS",
    "gender":"male",
    "love champion":"Varus"
})

print("Data added successfully")
print(result.inserted_ids)
print(result_solo.inserted_id)