thelist =["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thelist[2]="changed_value"

print(thelist)
thelist[1:2] =["change1", "change2", "change3", "change4"]
print(thelist)

list2 = ["zero", "one", "two", "three", "four", "five"]
list2[2:4]=[2,3,4]
print(list2)

list3=[0,1,2,3,4,5,6,7]
list3.insert(3,"inserted value")
print(" inserted to list 3 ", list3)