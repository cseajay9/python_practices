list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
print((list1+list2))

# using append method
for x in list2:
    list1.append(x)
print("using append in list1 ",list1)

# using list extend
lista = [1,2,3,4]
listb= ['A','B']
listb.extend(lista)
print("extended list b with a :", listb)

"""
append() adds an element at the end of the list
clear() removes all the elements in the list
copy() returns a copy of list
count() returns no. of elements with specified value
extend() add the elements of a list (or any iterable), to the end of the current list
index() returns the index of the irst element with the specified value
insert() adds an element at the specified position
pop() removes the element at specified postion, if not mentioned the last element
reversr() reverse the order
sort() sorts the list
"""