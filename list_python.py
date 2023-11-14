list1 = [10,20,30,40]
list2 = [10,"masud",[10,20,30]]

# show single elmenet of List
print("Access Single Element Of List: ",list1[2])
print("Access list Element Of List: ",list2[2][2])
print("Access Full List: ",list1)
lenth = len(list1)

for i in range(lenth-1,-1,-1):
    print("Access List Element in Decending Order: ",list1[i])

for i in range(lenth):
    print("Access List Element in Accending Order: ",list1[i])
    
# List Function Given Below:

del list1[0]
print("After delete o index from list:",list1)
list1.pop(0)
print("After pop from list:",list1)
list1.remove(30)
print("After remove from list:",list1)
list1.append(60)
print("After append in list:",list1)
list1.insert(0,90)
print("After append in list:",list1)
list1.append(list2)
print("After append in list:",list1)
list1.extend(list2)
print("After extend in list:",list1)
list1.clear()
print("After clear in list:",list1)

