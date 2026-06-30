                                             #input formatting from user#
'''
--->input()
--->the input()function is used to take input from the user

1.int()
ex:num = int(input("enter a number:"))
num3 = int(input("enter a number:"))
num2 = 89
print(num + num2 + num3)

2.string()
ex:hi = input("enter a char:")
print(hi + "python")

3.float()
ex:num = float(input("enter your salary:"))
print(num,"this is ur month salary")

4.list
ex:group = list(map(int,input().split()))
print(group)

5.tuple
ex:some = tuple(map(int,input("enter:").split()))
print(some)

6.eval
ex:num = eval(input("enter:"))
print(num,type(num))

7.using moduls%
ex:name = input("enter your name:")
age = int(input("enter your age:"))
print("my name is %s and i'm %d year old" %(name,age))

8.using comma ,
ex:name = input("enter your name:")
age = int(input("enter your age:"))
print("your name is",name,"your age is",age)


'''
name = input("enter your name:")
age = int(input("enter your age:"))
print("your name is",name,"your age is",age)
print("my name is %s and i'm %d year old" %(name,age))











