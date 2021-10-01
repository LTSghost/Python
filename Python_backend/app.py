#pip install Flask  安裝 Flask 套件

from flask import Flask #引入Flask 
from flask import request #引入request 物件
from flask import redirect #引入redirect 函式
from flask import render_template #引入render_temple 函式
from flask import session #引入 session 工具
import json #引入json模組
#建立Application物件......可以額外建立靜態檔案的路徑
app = Flask(
    __name__,
    static_folder = "public", #靜態檔案對應的資料夾
    static_url_path= "/abc"   #靜態檔案對應的網址路徑
)
#所有在 static 資料夾底下的檔案, 都對應道網址路徑。/static/檔案名稱

app.secret_key = "This is a secret."  #設定 session 密鑰

@app.route('/page2')
def templates_index2():
    return render_template('page2.html')

@app.route('/templates0')
def templates_index0():
    return render_template('index', name = "LTS")

@app.route('/templates1')
def templates_index1():
    return render_template('page1.html')

@app.route('/en/')
def index_en():
    return json.dumps({     #字典轉換json格式字串
            "text":"Home Page", #回傳路徑 / 的內容
            "status":"OK"
        })

@app.route('/zh/')
def index_zh():
    return json.dumps({
            "text":"首頁",
            "status":"OK"
        }, ensure_ascii = False) #指示不要用ASCII碼編譯成中文

@app.route("/") #建立路徑 / (根目錄)回應方式
def get_home(): #用來回應路徑 / 的處理函式
    # return redirect('https:/www.google.com/')  #導向到指定網址
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
        return redirect('/en/')
        
    else:
        return redirect('/zh/')


@app.route("/data")
def get_Data():
    return "Data here" #回傳網站路由/data的內容

@app.route("/user/<name>") #建立路由動態回應
def get_Name(name): #設定參數
    if name == "Howard":
        return "Hello " + name
    else:
        return "Hey " + name + ", Where is Howard?"

#利用要求字串(Query String) 提供彈性
@app.route("/getSum")
def getSum():
    minNum = request.args.get("min",1)
    minNum = int(minNum)
    maxNum = request.args.get("max",100)
    maxNum = int(maxNum)
    result = 0
    for i in range(minNum,maxNum+1):
        result += i
    print(result)
    return str(result)

@app.route('/accumulate', methods = ['GET'])
def accumulate():
    maxnum = request.args.get("Max", 5) #接收 GET 方法的 Query String
    maxnum = int(maxnum)
    result = 0
    for n in range(1,maxnum+1):
        result += n
    return render_template('/result.html', data = result)
    
    #"累加結果為: " + str(result)

# 使用 POST 方法 處理路徑 /accumulate2 的對應函式
@app.route('/accumulate2', methods=['POST'])  
def accumulate2():
    maxnum = request.form["Max2"]   #接收 POST 方法的 Query String
    maxnum = int(maxnum)
    result = 0
    for n in range(1,maxnum+1):
        result += n
    return render_template('/result.html', data = result)


@app.route('/Hello')
def Hello():
    session_name = request.args.get('name', "")
    session['user_name'] = session_name #session[欄位名稱] = 資料
    return "Hello," + session_name

@app.route('/talk')
def talk():
    name = session['user_name']        #抓取存放在session的資料
    return "嗨~ " + name + " 你怎麼在這!"

app.run(port = 3000) #啟動網站伺服器 , 可透過 port 參數指定埠號