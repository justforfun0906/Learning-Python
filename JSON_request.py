import requests
import json
response = requests.get("https://www.ccxp.nthu.edu.tw/ccxp/INQUIRE/JH/OPENDATA/open_course_data.json").json()
print (type(response));
print (response[0])
for x in response :
    print(x["科號"])
    print(x["課程中文名稱"])
    print("學分數：{}, 教師：{}".format(x["學分數"], x["授課教師"]))