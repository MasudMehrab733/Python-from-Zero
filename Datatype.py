my_set = {1,2,3,4,5}
#create two set from my_set
set1 = my_set.union({1,2,3})
set2 = my_set.intersection({5,10})
print("Original set: ", my_set)
print("set one is: ", set1)
print("set two is: ", set2)
add = my_set.add(10)
print(my_set)
remove =my_set.remove(5)
print(my_set)