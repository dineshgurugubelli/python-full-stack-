#Data types:

#int
#n=8

#float
#n=2.5

#string
#---->it is a sequence of char that are enclosed with " ",' ',""" """.
'''
num = "python"
print(num)
'''

#concatination
#---->Concatenation means joining strings together.
'''
so = "python"
any = " is a language"
print(so + any)
'''

#indexing
#---->Indexing lets you access individual characters in a string by their position.
#---->Positive indices start at 0 (leftmost character) and count rightward.
#---->Negative indices start at -1 (rightmost character) and count leftward.

hi = "python is language"
print(hi[12])

hi = "python is language"
print(hi[-12])

#methods:

#1.replace()
#----> returns a new string with occurrences of a substring replaced by another substring.
#syntax--->(name.replace(substring,substring))

hi = "python is language"
print(hi.replace("python","java"))

#2.join()
#---->combines elements of an iterable (like a list or tuple) into a single string, using the string it's called on as the separator.
#syntax---->("-".join(name of the variable))

hi = "python is language"
print("$".join(hi))

#3.split()
#---->breaks a string into a list of substrings based on a separator.
#syntax--->variable_name.split("substring")

hi = "python is language"
print(hi.split("is"))

#4.count()
#----> this method counts how many times a value appears.
#syntax---->variable_name.count("substring")

hi = "python is language"
print(hi.count("a"))

#string function:

#1.len()
#---->this will be find the length of the string

hi = "python is language"
print(len(hi))

#2.max()
# ---> Returns the maximum character in the string.

so = "Python is a Language"
print(max(so))

#3).min()
# ---> Returns the minimum character in the string.

so = "Python is a Language"
print(min(so))



















