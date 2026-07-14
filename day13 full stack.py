'''
--->passing by value
def some(a):
    for j in a:
        print(j)
some([2,3,1])    

--->passing by reference
a=(1,2,3)
def some(a):
    for j in a:
        print(j)
some(a)

--->return keyword
In a funtion if a return is executed then it will exit from the function with certain returned values.
def some(b):
    return [5+b]
a=some(10)
c=some(130)
print(a)
print(c)

import builtins
builtin_funtions = [
    name for name in dir(builtins)
    if callable(getattr(builtins))]
print(buitin_funtions)
print(f"total built-in funtions are (len(builtin_funtions))")

                                             #Recursive Function#
 
'''
def name(num):
    if num == 1:
        return 1
    else:
        return num * name(num-1)
num = 4
print(name(num))
                                            





















