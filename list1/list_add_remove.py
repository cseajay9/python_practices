# to add an item to the end of the list, we use append() method

thislist=[1,2,3,4,5,6,7]
thislist.append(3)
print(thislist)

# extending the list
tropical = ["mango", "pineapple", "papaya"]
tropical.extend(thislist)
print("new tropical list: ", tropical)

# adding any iterable to list
lista = ["apple", "banana", "kiwi"]
tupleb=["cherry", "orange"]
lista.extend(tupleb)
print(lista)

# Removing list items
listr = [1,2,3,4,5,6,2]
listr.remove(2)
print(" first occurence only removed from list: ",listr)

# to remove specified index use pop()
listr.pop(2)
print("the poped list index 2: ",listr)

# if not specified, pop() remnoves last item
listr.pop()
print("pop with empty argument: ",listr)

# del removes specified index or the entire list

listd= [2,4,6,8,9]
del listd[3]
print("del list[3]: ",listd)