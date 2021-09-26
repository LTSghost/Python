from flask import Flask #引入Flask 
from flask import request #引入request 物件

#建立Application物件......可以額外建立靜態檔案的路徑
app = Flask(
    __name__,
    static_folder = "public", #靜態檔案對應的資料夾
    static_url_path= "/abc" #靜態檔案對應的網址路徑
)

#所有在 static 資料夾底下的檔案, 都對應道網址路徑。/static/檔案名稱


@app.route("/") #建立路徑 / (根目錄)回應方式
def get_home(): #用來回應路徑 / 的處理函式
    print("請求方法", request.method) #print在伺服器端
    print("通訊協定", request.scheme)
    print("主機名稱", request.host)
    print("完整的網址", request.url)
    print("瀏覽器和作業系統", request.headers.get("user-agent"))
    print("語言偏好", request.headers.get("accept-language"))
    print("引薦網址", request.headers.get("referrer"))
    print("使用者IP", request.remote_addr)
    lang = request.headers.get("accept-language")
    if lang.startswith('en'):
        return "Home Page" #回傳路徑 / 的內容
    else:
        return "首頁"

@app.route("/data")
def get_Data():
    return "Data here" #回傳網站路由/data的內容

@app.route("/user/<name>") #建立路由動態回應
def get_Name(name): #設定參數
    if name == "Howard":
        return "Hello " + name
    else:
        return "Hey " + name + ", Where is Howard?"


app.run(port = 3000) #啟動網站伺服器 , 可透過 port 參數指定埠號