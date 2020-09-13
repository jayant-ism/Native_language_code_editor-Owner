
#inport some stuff
import subprocess
import json 


#the number of extra keywords declared 
count = 0 

# dictionary for hindi to english words
dic = {} 

# dictionary for english to hindi words 
rev_dic = {} 

#loading the global dictionary later include the values for the included libraries 
with open("map.json") as json_file: 
     
    
    dic = json.load(json_file) 

#loding the reverse dictionary 
with open("rev_map.json") as json_file: 
    
    
    rev_dic = json.load(json_file) 


# for running a python 
def run() :
    subprocess.call([r'compil\command.bat'])


# for finding and declaring keywords 

def val( sr ) :
    global count 
    
    
    
    if sr in dic.keys() :
        return dic[sr] 
    
    count += 1 

    dic[sr] = "as" + str(count) 

    rev_dic[dic[sr]] = sr 

    return dic[sr] 


#for converting hindi text to english along with the added files 

def hindi_eng( strin ) :
    

    leng =  len(strin) 
    out  ="" 
    


    itr = 0 

    while itr <  leng : 
  
        

        if strin[itr] == "'" :
            while itr < leng : 
                if strin[itr] == "'" : 
                    out = out + strin[itr] 
                    itr += 1 
                    break 
                out = out + strin[itr] 
                itr +=1 
            continue 
        
        if strin[itr] == '"' :
            while itr < leng : 
                if strin[itr] == '"' : 
                    out = out + strin[itr] 
                    itr += 1 
                    break 
                out = out + strin[itr] 
                itr +=1 
            continue 

        if strin[itr] <= chr( 128 ) :
            out = out + strin[itr] 
            itr += 1 
            continue 
        cur = ""
        while itr < leng  : 
            if strin[itr ] ==" " or strin[itr ] =="(" or strin[itr ] =="{" or strin[itr ] =="["   :
                break 
            cur = cur + strin[itr] 
            itr+= 1 
        
        out  = out + val(cur) 

    return  out
    

#for converting the english to hindi along wiht the added files 
def eng_hindi(strin ) : 
    lis = conv(strin ) 
    out_lis =[] 

    for i in lis : 
        cnn =  rev_dic[i]
        out_lis.append(cnn ) 

    out =  rev_con(out_lis ) 
    return out 

def doi() :
    f = open("flags/input.txt", "r" , encoding='utf-8')
    st =  f.read()
    print(st)  
    st = hindi_eng(st )     
    
    out = open("compil/code.py" , "w")
    out.write(st) 
    out.close() 
    f.close() 
    run()

    f = open("flags\output.txt" , "w" ,  encoding='utf-8')

    st = open("compil\error.txt" , "r" ,  encoding='utf-8')

    ss = st.read() 
    f.write(ss) 

    st.close()

    st = open("compil\out.txt" , "r" ,  encoding='utf-8')

    ss = st.read() 
    f.write(ss) 

    st.close()
      
    
    f.close() 
 
doi() 

def running() : 
    while(1) :
        
        st = open("flags\inpready.txt" , "r" ,  encoding='utf-8')

        ss = st.read() 
        
        st.close()
        if ss == "1" :
            break
    
    st = open("flags\inpready.txt" , "w" ,  encoding='utf-8')

    st.write("0")
         
    st.close()

        

        
    doi() 

    st = open("flags\outready.txt" , "w" ,  encoding='utf-8')

    st.write("1")

        
    st.close()
        
    running()

running()