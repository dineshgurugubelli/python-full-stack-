'''                                           #Generators#

--->This generator is special function that function that returns the itertor. instead of returning all the valueat once
--->Here we are going to use yield keyword.

def some():
    yield 1
    yield 2
    yield 3
so = some()
print(next(so))
print(next(so))
print(next(so))

working of generator:
--------------------
--->when a funtion is called
--->it dose not execute the function immediatly....
--->it will not return the generator objiect
--->Then the funtion will pasuses at each yield..
--->When the next() is called again, execution resume from where it stoped

def demo():
    print("start")
    yield 1

    print("second")
    yield 2

    print("endd")
    yield 3
how = demo()
print(next(how))
print(next(how))

with Generator:
-------------

def how(so):
    for i in range(so):
        yield i*3
any = how(5)
print(next(any))
print(next(any))
print(next(any))

without generator:
------------------

def amo(so):
    for i in range(so):
        print(i)
how = amo(5)

Function:
--------
--->return
--->Return complete result
--->Function will end after the return the values
--->more memory usage
--->This function never resume

Generator:
---------
--->yeild
--->return one value at once
--->pauses after every yield
--->less memory usage
--->Resume after next().

yield keyword:
--------------
--->This will product the value
--->But the yield pasues the function
--->And yield will savve the function current state
--->yield will continues where it stoped.

def how (so):
    for i in range(so):
        yield i
any = how(7)
print(next(any))
print(next(any))
print(next(any))
print(next(any))


next keyword():
--------------
--->The next() function is used to retriieve the next value from next.

def how (so):
    for i in range(so):
        yield i
any = how(7)
print(next(any))
print(next(any))
print(next(any))
print(next(any))

Stopiteration:
-------------
--->Calling next() function after all values retreive then it will raise stopiteration exception.

def how (so):
    for i in range(so):
        yield i
any = how(7)
print(next(any))
print(next(any))
print(next(any))
print(next(any))

'''
def name(so):
      for i in range(so):
          yield i*3
          count = 0
          if i*3 ==0:
              print(i)
              count +=1
no = name(10)
print(next(no))
print(next(no))
print(next(no))
print(next(no)) 
    




















































    
