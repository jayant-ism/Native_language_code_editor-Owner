import json 

dic = {} 




cnt = int(input() ) 

for i in range(0 ,cnt ) : 
    y = input()
    z = input()
    dic[y] = z 



with open ("map.json" ,"w") as out : 
    json.dump(dic , out )  
