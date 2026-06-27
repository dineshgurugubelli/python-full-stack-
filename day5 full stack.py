'''                                            #Dictionary#
--->Dict is the key : value pair.
--->In the place of key we have use immutable data type.
--->dict is mutable.
--->Methods:

1.keys()
--->it is used to print the keys.
# ex : so = {"name":"afsa",
      "age":20,
      "gender":"female"}
print(so.keys())

2.values()
---->it is used to print the values.
# ex :so = {"name":"afsa",
      "age":20,
      "gender":"female"}
print(so.values())

3.items()
--->it is used to print the both keys and items.
#ex :so = {"name":"afsa",
      "age":20,
      "gender":"female"}
print(so.items())

4.clear()
---->it is used to delete all the data in the dict.
#ex :so = {"name":"afsa",
      "age":20,
      "gender":"female"}
      print(so.clear())

5.update()
--->it is used to update the values as well as keys also.
#ex : 

details ={"name":"dinesh",1:"number",(6,7) : [1,2]}
print(details)
so = {"name":"afsa",
      "age":20,
      "gender":"female"}
print(so.values())
print(so.keys())
print(so.items())
print(so)
so.update({"phn":1234567})
print(so)
'''
'''                                                  #sets#

--->set is collection unordered elements that are seperated by ,{}.
--->set is mutable.
--->can remove duplicate value itself.
--->methods:
1.union():(|)
--->combine the elements from both set
--->sytax:set.union(set2)
#ex : go = {1,2,3,4}
so = {4,5,6,7}
print(go|so)

2.intersection():(&)
--->comman elements from the both sets.
--->syntax:set.intersection(set2)
#ex: go = {1,2,3,4}
so = {4,5,6,7}
print(go & so)

3.symmetric difference():(^)
--->all different element from both sets.
--->syntax:set.symentric_difference(set2)
#ex: go = {1,2,3,4}
so = {4,5,6,7}
print(go^so)

4.add():
--->it is used to add new element.
#ex: go = {1,2,3,4}
go.add(5)
print(go)

5.remove():
--->to delete the element from set.
#ex:so = {4,5,6,7}
so.remove(4)
print(so)

6.discard():
--->discard will delete the value.
ex: go = {1,2,3,4}
so.discard(5)
print(so)

'''
go = {1,2,3,4}
so = {4,5,6,7}
print(go|so)
print(go & so)
go.add(5)
print(go)
so.remove(4)
print(so)
so.discard(5)
print(so)


























