t=(10,20,60,50,40,)

print(t)
print(type(t))

print(t[3])
l =len(t)
for i in range(l):
    print(t[i])
for i in t:
    print(i)
    
print("Maximum in Tuple:- ",max(t))
print("Minimum in Tuple:- ",min(t))
print("Sumation in Tuple:- ",sum(t))
print("Count Any Value in Tuple:- ",t.count(20))
print("Check Index of Any Value in Tuple:- ",t.index(50))


