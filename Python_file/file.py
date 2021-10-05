file = open("data.txt",mode="w",encoding = "utf-8")  # 開啟
file.write("Hello World \n this is index")  # 操作
file.close()  # 關閉

#使用 with 會自動進行檔案的關閉
with open("data.txt", mode = "w", encoding = "utf-8") as file:
    file.write("199\n299")

#全部讀取
with open("data.txt", mode = 'r', encoding = 'utf-8') as file:    
     data = file.read()

sum = 0
with open("data.txt", mode = 'r', encoding = 'utf-8') as file:
    for line in file:
        sum += int(line)

print(data)
print(sum)

import json

with open("config.json", mode = "r") as file:
    data = json.load(file)

print(data)

data["house"] = "red"

print(data)

with open("config.json", mode = 'w') as file:
    json.dump(data, file)

print("country:",data["country"])
