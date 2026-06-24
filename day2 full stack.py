'''
operaters
--------
1.arithmetic
2.assignment
3.comparison
4.logical
5.identity
6.membership
7.bitwise
'''
#arithmetic -,+,*,/,//,**,%
a=2
b=8
print(a+b)

#assignment =,+=,-=,*=,%=
a+=1
print(a)

#comparison >,<,<=,>=,==
print(a>=b)

#logical and, or ,not
#AND----->both must true
#OR------>At least one true
#NOT----->reverse the output

print(a==2 and b==5)
print(a==2 or b==5)
print(not b==5)

#identity is,is not
c=[6,5]
d=[6,3]
print(id(d))
print(c==d)
print(c is not d)
print(c is d)

#membership in,not in
print(a in d)

#bitwise &,>>,<<,|
z = 12
y = 10
print(z & y)   
print(z | y)   
print(z ^ y)   
print(~z)      
print(z << y)  
print(z >> y)  



















