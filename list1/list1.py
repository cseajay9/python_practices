""" python lists are ordered, changeable and allow duplicate values
 by order, it means items have a defined order and new items are appended at the end of the list
"""

thelist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thelist)

print("the lenght of thelist:",len(thelist))

list1 =["abc", 32, True, "Nepal"] # a list can contain different types of values
print(list1, "its type",type(list1))

# the list() constructor

mylist = list(("c", "c++", "Python", "Java"))
print(mylist)