#Inheritance:
#1.Single inheritance:
#----------------------
"""
class animal:
    def sound(self):
        print("animal make sound")
class dog (animal):
    def bark (self):
        print("dog bark")
d = dog()
d.sound()
d.bark()

example:
-------
class father:
    def gichi(self):
        print("i want to add",12+30)
class son(father):
    def lada(self):
        print("i want to sub",12-10)
faa = son()
faa.gichi()
faa.lada()

        
"""
#2.Multiple inheritance:
#-------------------------
"""
class father:
    def gichi(self):
        print("i want to add",12+30)
class child:
    def hoda(self):
        print("i want to multple",2*5)
    
class son(father,child):
    def lada(self):
        print("i want to sub",12-10)
faa = son()
faa.gichi()
faa.lada()
faa.hoda()
"""
#3.Multi-Level:
#---------------
"""
class grandfather:
    def gichi(self):
        print("own house",12+30)
class father(grandfather):
    def dinesh(self):
        print("my house",12*2)
class son(father):
    def lada(self):
        print("3bhk",12-10)
faa = son()
faa.dinesh()
"""
#4.Hierarchical:
#----------------
"""
class mother:
    def show_(self):
        print("10kg")
class affu(mother):
    def show2(self):
        print("5kg")
class affrin(mother):
    def show3(self):
        print("remaining part")
child1=affu()
child2=affrin()
child1.show_()
child2.show2()
"""
#5.Hybrid inheritance:
#--------------------
"""
class a:
    def methodA(self):
        print("A is a single")
class b(a):
    def methodB(self):
        print("B is double")
class c(b):
    def methodC(self):
        print("C is triple")

s1= c()
s1.methodA()
"""
#6.super():
#----------
"""
class dinesh:
    def dii(self):
        print(12*2)

class affu(dinesh):
    def aff(self):
        print(12*34)

class affrin(affu,dinesh):
    def arr(self):
        super().aff()
        super().dii()
        print(1*2345)

d1 = affrin()
d1.arr()


































