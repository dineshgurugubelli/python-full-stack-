#---------------File Handling-------------------#
'''
File handler is an object that gives more options like creating, updating.

Two ways to open the file....
-------------------------------
1)open()
----------
Syntax--> do = open('file_name','mode')

          close()
Example :
with open('demo.txt','r') as do:
    print(do.read())          

2)with(keyword)

Syntax ---> with open('file_name','mode') as do:

* Modes
-------
--> 'r'-- Used to read the file, incase if the file is not present it will raise error.
     Eg: with open('demo.txt','r') as do:
            print(do.read()) 

--> 'w'-- Used to write the text inside the file..
       -- Incase if the file is not present it will create a new file with name givenn

--> 'a'-- This Used to to add the text at last position inside the file..
     Eg:  with open('demo.txt','a') as do:
          print(do.write('\nWe are working on File Handling'))

--> 'x'-- used to create a new by adding the inside the file, incase if the file is present it will raise an error.....
     Eg:     with open('demo1.txt','x') as do:
                 print(do.write('\nWe are working on File Handling in python session'))


Write()
--------
--> This function is used to add the text inside a file or updates a file with new Text....
Example:-
with open('demo.txt','r') as do:
            print(do.read())
with open('demo.txt','a') as do:
          print(do.write('\nWe are working on File Handling'))

* read()
---------
--> Used to read a file and this read() will read file chunk by chunk...
    We can also specify the size
    Example:with open('demo.txt','r') as do:
                print(do.read(10))


*readline()
--------------
-->This readline() function will be read only one line at a time...
Example: with open('demo.txt','r') as do:
             print(do.readline())

*readlines()
---------------
This readlines() function will be read Total File and will give as a list where each is line is taken as single index...
Example:-
with open('dem.txt','r') as do:
    print(do.readlines())

'''
