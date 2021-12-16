# offer a shorter syntax when we want to create a new list based on the values of existing one

fruits =["apple", "banana", "cherry", "kiwi", "mango", "apricot"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)


newlist1 = [y for y in fruits if "a" in y]
print("\n",newlist1)


newlist2 = [z for z in fruits if z!= "apple"]
print("\n excluded apple: ",newlist2)

# iterable can be any iterable object, like a tuple, list, set etc
# using range funciton we can create an iterable

iterable=[x for x in range(10)]
print("\niterable",iterable)

# return some other value instead of original value
changed=[x if x!="apple" else "orange" for x in fruits]


change1=[x for x in fruits if "a" in x]
print("changed apple to orange",changed)
print("fruits containing 'a' ", change1)