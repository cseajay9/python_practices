thelist = ["apple", "mango", "guava"]
for x in thelist:
    print(type(x),x)
print("\n")
# looping through items by referring their index no.

for i in range(len(thelist)):
    print(type(i),"index[", i ," ]", thelist[i])



# using while loop
print("\n using while loop")
a =0
while a < len(thelist):
    print(thelist[a])
    a += 1
print("\n")

# list comprehension offers the shortest syntax for looping through lists:
print("using list comprehension: ")
[print(y) for y in thelist]