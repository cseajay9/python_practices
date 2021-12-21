# once tuple created, items in it can't be changed, added or removed,
# however converting it into list, updates or modification can be done, and again revert to tuple

x = ("apple", "bananna", "cherry", "kiwi")
y = list(x)
y[2] = "orange"
x = tuple(y)

print(x)

# items can't be added, but two tuple can be added together
tuple1 = ("apple", "kiwi")
tuple2 = ("orange",)

tuple1 += tuple2
print("tuple1 + tuple2 ",tuple1)
