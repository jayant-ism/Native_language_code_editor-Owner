from django.shortcuts import render
from django.http import HttpResponse

prev_ceod = []

#inport some stuff
import subprocess
import json 

# Create your views here.
def  main(request) : 
    return render(request ,'home.html' )  


def  eval(request) : 

    print(request.GET['code']) 

    strin =  request.GET['code'] 
    
    out = open("hindi_english/flags/input.txt" , "w" ,  encoding='utf-8')
 
 
 
    out.write(strin)

    out.close() 
    
    print(strin)

    
    out = open("hindi_english/flags/inpready.txt" , "w" ,  encoding='utf-8')
 
 
 
    out.write("1")


    out.close() 


    while(1) :
        
        out = open("hindi_english/flags/outready.txt" , "r" ,  encoding='utf-8')
 
        ss= out.read()
        out.close()

        if ss == '1' :
            break 

    out = open("hindi_english/flags/output.txt" , "r" ,  encoding='utf-8')
 
    
 

    ans = out.read()


    out.close() 
    
    print(ans) 

    
    
    out = open("hindi_english/flags/outready.txt" , "w" ,  encoding='utf-8')
 
 
 
    out.write("0")


    out.close() 


    asd = [strin  , ans ]
    prev_ceod.append(asd ) 

    ddsr =[] 



    f = open("hindi_english/map.json" , encoding="utf-8")
    
    v =  json.load(f) 

    for k in v.keys() : 
        sda = [ k , v[k] ] 
        ddsr.append(sda) 






    return render(request ,'home.html' , {'prev_ceod' : prev_ceod , 'map' : ddsr } )  