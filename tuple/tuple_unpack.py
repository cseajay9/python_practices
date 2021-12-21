# when we create a tuple, we assign values to it, this is called "packing" a tuple:
# but python allows us extract values back into variables, this is called unpacking.

fruits = ("apple", "banana", "kiwi", "lemon")
(green, yellow, red, cyan) = fruits # no. of variable should be equal to no. of items,
print("yellow: ", yellow)

# if no. of varaible is less than item no, add prefix * to variable name and that will become list wth remaining items

(a, b, *c) = fruits
print("\ntype of a , b , c ",type(a), type(b), type(c))

(*b,)= fruits # this way we can convert tuple into list
print(type(b),b)

(one, *list, two) = fruits # this way, "one" gets first elemlent, "two" gets last elemelnt and remaining is convereted to list
print(one)
print(list)
print(two)
