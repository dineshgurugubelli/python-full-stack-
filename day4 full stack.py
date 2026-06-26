                                                   #List#

#--->list is a collection of different datatype that are enclosed in [].
#--->list is mutable it is changeble without using modifing

# muttable                                     immutable
#the datatype can be modified               can't be modified 
#list                                        string  
#ex_type = [1,'python',[1,2]]

#--->methods in list

#1.append() add the new item to the list.
#---->it will add in the last position of index and it will add at a time only one item.
'''
so = [1,2,3,4]
print(so)
so.append(5)
print(so)
so.append("python")
print(so)
'''
#2.extend()
#--->this is also add items in this list index,but it will give each value in the each index position.
'''
so = [1,2,3,4]
print(so)
so.extend("pyhton")
print(so)
'''

#indexing, count,insert (method)

'''
so = [1,2,"python is language",[45,78,"java is a language",[1,23],90],"hello"]
print(so[3])
print(so[3][2])
print(so[3][2][10])
'''

#4.pop()
#--->it is used to remove the value from the list, but it based on the indexing.
#--->variable.name.pop(index position)
'''
so = [1,2,40,90,35]
so.pop(3)
print(so)
'''

#5.remove()
#--->it is used to delete the item from the list,but it will remove the direct value.
#--->variable.name.remove(value)
'''
so = [1,2,40,90,35]
so.remove(40)
print(so)
'''

#6.insert()
#--->it is used to add item at specific position.
#--->variable.name.insert

so = [1,2,40,90,35]
so.insert(3,55)
print(so)

                                                    #Tuple#

#--->tuple is a collection of different datatype represent in ().and seperated by (,).
#--->it is immutable
#--->methods are indexing,count. 
#index(),count().
'''
how =(1,2,3,4,"python",[4,5],(90,54))
print(how.count(4))
print(how.index("python"))
'''
'''
my = [45,65,12,76]
print(sorted(my))
print(my)
my.sort()
print(my)
'''



























