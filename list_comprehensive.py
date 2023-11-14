a =[]

for i in range(1,101):
    a.append(i)

print(a)

# Using Comprehensive

b =[i for i in range(1,101)]

print(b)

c = [i for i in range(1,101) if (i%2==0)]

print(c)