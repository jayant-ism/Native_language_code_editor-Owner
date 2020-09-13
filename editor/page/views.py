from django.shortcuts import render
from django.http import HttpResponse

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
    
    
    out = open("hindi_english/flags/inpready.txt" , "w" ,  encoding='utf-8')
 
 
 
    out.write("1")

    out.close() 


    while(1) :
        inc =1 
        out = open("hindi_english/flags/outready.txt" , "r" ,  encoding='utf-8')
 
        ss= out.read()
        out.close()

        if ss == '1' :
            break 

    out = open("hindi_english/flags/output.txt" , "r" ,  encoding='utf-8')
 
    
 
    ans = out.read()


    out.close() 
 
    
    
    out = open("hindi_english/flags/outready.txt" , "w" ,  encoding='utf-8')
 
 
 
    out.write("0")


    out.close() 
     
    print(ans)

    return render(request ,'home.html' )  