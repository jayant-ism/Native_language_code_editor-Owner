![GitHub Logo](https://github.com/jayant-ism/Native_language_code_editor-Owner/blob/master/img/logo.jpg)

# Native language code editor 

## What is Native language code editor  ?? 
Native language code editor is a code editor that  allows us to code any programming language in our native language.

We can code python , java script , c++ etc in our natvie language like hindi,telgu,tamil.

## Why Native language code editor  ??

We aim to remove the barrier of language from the IT sector. Along with its easy to code in the language that a person is most familier with.
We provide options for choosing the programming languages and the respective native language

This project aims at running the python code. We can process different languages just by specifying the compiler used in
** "editor\hindi_english\compil\command.bat" ** file and changing the respective file name in the doi function of the main.py .


## How to use it :
Make sure that the keywords that are going to be used is alright
If not, one can add/ change/ remove by running to to_map.py in  " **editor\hindi_english** "  directory after it
    we just have to give input as "n" in first line denoting number of parameters we need to change 
    followed by next n line containing 2 words one in native language and other in english for the keyword of the programing language. 


After it we need to run "**editor\hindi_english\main.py**" the backend surver which is responsible for running and processing the code.
After it we need to launch the django server through the command prompt code  **python manage.py runserver**  in the editor directory.

Once it is done we just need to write our code in any native language the backend server will automatically match it throught the keywords
and compile it then execute it We need not to select the native language used , but for help a box is provided with all the keywords in native
language mapped to those in the english.

Then just press run 

Your code along with the output  and error will be displayed and the code arena will be cleared.

## GUI description
![GitHub Logo](https://github.com/jayant-ism/Native_language_code_editor-Owner/blob/master/img/Screenshot%20(132).png)

The top portion contain the part of the code that was exicuted just before along with the results 
Then comes the coding arena where we can put our code in any language. 
At the right we have the keywords that we chose.

## Dependencies 
1. Django 
2. Compiler of the language that you are going to use


##Demo Link :- https://drive.google.com/file/d/1m1oCvlzfCipVhcXMhun_6suvToYBWNiG/view

