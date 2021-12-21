# indexing is similar to list, using index no. in square bracket and -ve index is used for referring items from last
thistuple = ("apple", "banana", "mango", "cherry")
print("thistuple[1] gives: ",thistuple[1], " , and via -ve index: [-2]: ",thistuple[-2])

# using range of index
tuple_range =("apple", "banana", "cherry", "guava", "lemon", "kiwi", "orange")
print("original tuple ",tuple_range)
print("tuple[2:4] ", tuple_range[2:4])
print("tuple[:4] ", tuple_range[:4])
print("tuple[2:] ", tuple_range[2:])

#checking items in tuple
if "apple" in tuple_range:
    print("yes, 'apple' is in the tuple")

