'''                                            #funtions#
--->funtions is a block of code that can be resuble.
--->funtion can avoid the repeated line of code.
funtions are two types:

1.built-in:
ex:print(),max(),type(),min(),max(),sum().

2.user-define:
--->this function starts with keyword(def).
ex: def function_name(num):
    ------------
    ------------
--->function_name(arguments)

ex: def add(a,b):
    print(a+b)
add(2,4)

--->Types of arguments:
1.Requered arguments
-->we have to pass same number argument with defination of the function.
ex:def add(a,b):
    print(a)
add(2)

2.default
-->
ex: num=7
num_2=3
num_3=4
def add(a,b,c):
    print(a+b+c)
    print(b)
    print(c)
add(num,num_2,num_3)

3.keyword
-->we can pass as a pair like(var=datatype)
ex:def add(a,b):
    print(a+b)
add(a="pyth",b="on")
add(a=5,b=5)

4.variable length
-->can pass n number of arguments and just (*args) in the parameter, will receive tuple of arguments.
ex:num=7
num_2=3
num_3=4
def add(*a):
    print(a[1])
add(num,num_2,num_3)

ex:num=7
num_2=3
num_3=4
def add(*a):
    print(a)
add(num,num_2,num_3)

---->when we use the single star(*arg)=tuples.
--->when we use double star (**arg)=dictonary.
ex: def all(**any):
    print(any["name"])
all(name="dinesh",age=14)

--->Global variable:
it is used for throught the funtion.
ex:num = 9
def name():
    print(num)
name()

--->local variable:
--->it is used to inside the func.
ex:def name():
    num = 9
    print(num)
name()
note
--->to change the global variable by using keyword (global)that can be changble completly inside andd outside 
ex: num = 9
def name():
    num = 34
    print(num)
name()
print(num)

ex:num = 9
def name():
    global num
    num = 34
    print(num)
name()
print(num)
'''
num = 9
def name():
    global num
    num = 34
    print(num)
name()
print(num)












