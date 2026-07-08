'''                                               #loops#        
1.for loop
--->A for loop is used to itterated over a squence ,list,tuple,dict.

else in foe loop:
---> the else block will executed after thr for loop,but incase the loop is breaked print only for loop.

ex:so = "pyhton is a language"
for j in so:
    print(j)

do = [1,2,3,4,5,6,7]
for m in do:
    print(m)

d = {"name":"dinesh",
     "age":"89",}
for i in d.keys():
    print(i)


2.while loop
--->the condition will be satisfiye until it will print. 
ex:i = 1
while i < 5:
    print(i)
    i +=1

                                           #control statements#
1.break
--->the break is used to exit from the loop.

a = [1,2,3,4,5]
for j in a:
    print(j)
    if j == 3:
        break
else:
    print("three")

2.continue
--->The continue will skip the current itteration.
a = [1,2,3,4,5]
for j in a:
    if j == 3:
        continue
    print(j)
else:
    print("three")

3.pass()

a = [1,2,3,4,5]
for j in a:
    if j == 3:
        pass
    print(j)
else:
    print("three")

4.range()
for i in range(1,23,2):
    print(i)

5.assert()
a = int(input("enter the number:"))
assert em > 6,"it having error"



                                            

'''



a = 0
while a < 100:
    a+=2
    print(a,end=" ")










    
