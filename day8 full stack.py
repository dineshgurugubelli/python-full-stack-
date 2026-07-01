'''                                           #statments#
                                                   |
                                            ---------------       
                                            |             |
                                     conditional         looping
                                     if                  for  
                                     if-else             while
                                     elif
                                     break
                                     continous



1.condition statement:
--->if

ex:d = 10
if d % 2 ==0:
    print(d,"is even")

--->if-else
-->else is the fall-back statement incase if condition false else will be only excuted.

ex:d = 11
if d % 2 ==0:
    print(d,"is even number")
else:
    print(d,"is odd number")

ex2:dinesh_ICIC_details = {"ATM PIN":'6600'}
pin = input("enter your pin:")
if pin in dinesh_ICIC_details['ATM PIN']:
    print("welcome")
else:
    print("pin wrong")
    
--->nested if  if condition having another if condition.

ex:dinesh_ICIC_details = {"ATM PIN":'6600'}
pin = input("enter your pin:")
if len(pin)==4:
    if pin in dinesh_ICIC_details['ATM PIN']:
        print("welcome")
    else:
     print("pin wrong")
else:
    print("enter only 4 digit pin")

--->elif

ex:marks = int(input("enter marks:"))
if marks >=90:
    print("a+")
elif marks >=80:
    print("b+")
elif marks >=70:
    print("c+")
else:
    print(" you are fail")

=>find out the max number among 3.

num1 = int(input("enter your number:"))
num2 = int(input("enter your number:"))
num3 = int(input("enter your number:"))
if num1 > num2:
    print(num1,"is greater")
elif num2 > num3:
    print(num2,"is greater")
elif num3 > num1:
    print(num3,"is greater")
else:
    print("in valid")
'''
d = input("enter a char:")
c = "a,e,i,o,u,A,E,I,O,U"
if d in c:
    print(d,"it is vowels")
else:
    print("it is not a conconet")
    

              








              

    
