                                            #Type converstion#

'''
This is process of converting one data typr to another.
Int----> string,Float

ex:num=89
 num2=float(num
 print(num2)
 print(type(num))
 word=str(num)
 print(word)

float--->string,integer
ex:num=8.9
  how=str(num)
  print(how)
  print(type (how))
  flo=int(num)
  print(flo)
 
string--->Interger,float,list,tuple
ex:hai="78"
  num=int(hai)
  pritn(num+10)
  hello="67.89"
  num2=float(hello)
  print(num2+num)

  any="23456"
  con=list(any)
  print(con)
  con1=tuple(any)
  print(con1)

list--->string,tuple
ex:num=["p",'y','t','h','o','n']
  con="".join(num)
  print(con)
  some=tuple(num)
  print(num)

  pyth=[("a",1),('b',8)]
  conv=dict(pyth)
  print(conv)


tuple--->string,list
ex:fam=(1,2,3,4)
 print(list(fam))
 tup=('b','h','a','r','a','t')
 text="".join(tup)
 print(text)

                                #Built in functions#

1. str()
2. float()
3. int()
4. list()
5. dict()

'''
num = "python"
print(list(num))
so = "123456"
print(tuple(so))

do = ["p","h","j"]
con = "".join(do)
print(con)

do_2 = ('p','o','i','u','y')
do_ = str(do_2)
print(do_)

din = [('a',1),('b',4)]
conve = dict(din)
print(din)














