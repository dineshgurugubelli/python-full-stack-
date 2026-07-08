#prime numbers#
'''
num = int(input("enter a number:"))
count = 0
for i in range(1,num+1):
    if num % i == 0:
        count +=1
if count == 2:
    print(num,"it is prime number")
else:
    print(num,"it is not a prime number")

#prime numbers#

limit = int(input("enter a number:"))
for i in range(1,limit+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count +=1
    if count == 2:
        print(i,"it is prime")

#right angle traingle#

num = 5
for i in range(num+1):
    for  j in range(i+1):
        print("*",end="")
    print()

num = 5
for i in range(1,num+1):
    count = 0
    for  j in range(1,i+1):
        count += 1
        print(count,end=" ")
    print()

#amstrong number#

am = int(input("enter a number:"))
length = len(str(am))
saa = 0
for i in str(am):
    saa += int(i)**length
if saa == am:
    print(saa,"is a amsttr")
else:
    prrint(saa,"is not amstronng")

num = 10
for j in range(num):
    print(" "*(num-j-1),end=" ")
    print("*"*(2*j+1))



prime = int(input("enter the number:"))
count = 0
for i in range(1,prime+1):
    if prime % i == 0:
        count +=1
if count == 2:
    print(prime,"it is a prime number")
else:
    print(prime,"it is a not prime number")
     
       
num = int(input("enter the number:"))

count = 0
for i in range (1,num+1):
   if num % i==0:
       count +=1
if count == 2:
    print("it is prime")
else:
    print("it is non prime")



limit = int(input("enter a number:"))
for i in range(1,limit+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count +=1
    if count == 2:
        print(i,"it is prime")

num = int(input("enter a number:"))
for i in range(num):
    for j in range(i+1):
        print("*",end=" ")
    print()


num = int(input("enter the number:"))
for i in range(1,num+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
if count ==2:
    print("it is a value")
else:
    print("it is a non valye")

'''
can = int(input("enter a number:"))
count=0
for i in range(1,can+1):
   if i % 2 == 0:
       count+=1
       
       print(i)

    
























