try:
    num= int(input("enter a number:"))
    num2=int(input("enter a number:"))
    num3= num/num2
    print(num3)
except NameError:
    print("it having name error")
except ValueError:
    print("it having value error")
else:
    print("no error")
finally:
    print("nenu elagina print avutha ra puka")
