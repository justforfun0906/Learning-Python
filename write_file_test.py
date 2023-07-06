fn = 'c_chat_title.txt'
file_Obj = open(fn , 'w',encoding='gb18030',errors='ignore')
file_Obj.write("test")
file_Obj.close()
file_Obj = open(fn)
data = file_Obj.read()
file_Obj.close()
print(data)