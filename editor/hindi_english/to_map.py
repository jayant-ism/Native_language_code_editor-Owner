import json 

dic = {} 

rev_dic = {} 



cnt = int(input() ) 

for i in range(0 ,cnt ) : 
    y = input()
    z = input()
    dic[y] = z 
    rev_dic[z] = y 



with open ("map.json" ,"w") as out : 
    json.dump(dic , out )  
with open ("rev_map.json" ,"w") as out : 
    json.dump(rev_dic , out )  
