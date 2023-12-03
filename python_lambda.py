
x = lambda a:a+3

def sum(n):
    return lambda a:a*n

s = sum(9)    
print(x(9),s(3))