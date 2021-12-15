"""
list is a collection which is ordered, changeable and allows duplicate members
Tuple is a collection which is ordered, unchangeable, and also allows duplicate members
Set is unordered, unchangealbe*, and unindexed. No duplicate members
Dictionary is ordered * and changeable. No duplicate members
"""
mylist = ["zero","one", "two", "three", "four"]
print("normal indexing: ",mylist[3], "negative indexing [-3]",mylist[-3] )

# Range of index, specifying the start and where to end, return value is a new list

thislist=["apple", "banana", "cherry", "orange", "kiwi","mango"]
print("range [2:5] 2 included and 5 excluded: ",thislist[2:5])
print("\n when nothing mentioned, starts at 0, [:4]:  ", thislist[:4])

print("using neg index range [-5:-1]",thislist[-5:-1])
# whatever be the indexing pos or neg, it should be traversed in L-R fashion of the list

# checking in the list
newlist=["one", "two", "three","four","five"]
if "one" in newlist:
    print("yes, it is in the list")

