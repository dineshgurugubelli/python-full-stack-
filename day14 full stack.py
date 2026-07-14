'''                                            #lambda#
--->This is also called as annonymous function.
--->A lambda funtion can take n number of arguments but having only one expression.
syntax:
--->lambda argumrnts : expressions
some = lambda an,so,why : an + so * why
print(some(10,2,22))


filter()
--------
--->The filter() funtion is built-in funtion used to filter used to elements from an itterables such as list, tuple and set
besd on condition.

syntax:--->filter(funtion,itterable)
--->This filter() funtion returns filter object so we can convert that integr,list,set,tuple. 

#even number to print using filter().
num=[2,3,4,5,1]
rev = filter(lambda a:a%2==0,num)
print(set(rev))

#odd numbers to print using filter().
num=[2,3,4,5,1]
rev = filter(lambda a:a%2!=0,num)
print(set(rev))

list comprehenses
-----------------
--->This offers a shorter syntax when we want to create a how dict from the old dict.

syntax-->variable_name = [expression loop]
old_dict = {1:2,3:7,6:7}
new_dict = {i:j for {i,j} in old_dict.items() if j%2 ==0}
print(new_dict)

'''




































