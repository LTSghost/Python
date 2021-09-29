#pip install pymongo[srv]  安裝 Python 連接 MongoDB 套件    !!要從powershell去安裝pymongo
import pymongo  #引入 pymongo 套件

#連線到 MongoDB 雲端資料庫
client = pymongo.MongoClient("mongodb+srv://LTSghost:limitless123@mycluster.yqjkg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test #選擇操作 test 資料庫
collection = db.users #選擇操作 users 集合

#把資料新增至集合 json格式
collection.insert_one({
    "name":"LTSghost",
    "gender":"male"
})
print("Data added successfully")