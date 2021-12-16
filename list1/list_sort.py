thislist = ["orange", "mango", "kiwi", "pineapple", "banana" ,"Apple", "apple","Banana"]
thislist.sort()
revlist =[x for x in thislist]
print(thislist)
revlist.sort(reverse=True)
print("rev list",revlist)

# for case insensitive sort

ilist = ["orange", "mango", "Kiwi", "kiwi","pineapple", "banana" ,"Apple", "apple","Banana"]
ilist.sort()
print(ilist)