import webbrowser
import requests
import re
from bs4 import BeautifulSoup
url = 'https://www.ptt.cc/bbs/C_Chat/index17642.html'
base = 'https://www.ptt.cc/bbs/C_Chat/index'
out_file = 'c_chat_title.txt'

ind = 17642
for i in range(ind,17600,-1):    
    the_url = base+str(i)+'.html'
    print("url = %s"% the_url)
    htmlfile = requests.get(the_url)
    if htmlfile.status_code == requests.codes.ok :
        print("requested successfully")
        objSoup = BeautifulSoup(htmlfile.text, 'html5lib')
        objTitle = objSoup.find_all("div", class_="title")
        file_obj = open(out_file,'a',encoding='utf_16', errors='ignore')
        file_obj.write("url = "+ the_url)
        for data in objTitle:
            #print(data.text)
            file_obj.write(data.text)
        file_obj.close()        
    else :
        print("failed")
    