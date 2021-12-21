# Python tuple is a collection which is ordered (items have defininte order) , and
# unchangeable ( add, or remove not allowed)
# since they are indexed, items can be duplicate

thistuple = ("apple", "banana", 1, "cherry")
print(thistuple)
print("length of tuple:", len(thistuple))
print(thistuple[3])

# tuple with one element must have a , at the end else it is not conisdered tuple
tuple1=("apple",)
print("tuple1 is", type(tuple1))

tuple2=(3)
print("tuple 2 is ", type(tuple2))

# creating tuple using tuple() constructor
t1 = tuple(('apple', 'ball', 'cat',5))
print("tuple t1: ",t1)

