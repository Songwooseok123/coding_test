file = open("./20250221.txt","w",encoding = "utf8")
file.write("안녕")
file.close()

file = open("./20250221.txt","a",encoding = "utf8")
file.write("\n이어서 쓰는건 'a'")
file.close()


# 전체 읽기 
file = open("./20250221.txt","r",encoding = "utf8")
data = file.read()
print(data)
file.close()


# 한줄씩 읽기 
file = open("./20250221.txt","r",encoding = "utf8")
while True:
    
    data = file.readline()
    print(data)
    if data ==""  :
        break
file.close()
