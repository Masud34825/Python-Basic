dic = {
    "name":"masud",
    "age": 30,
    "course":"python"
}

print(dic)
print(dic.get('course'))
for i in dic:
    print(dic[i])
for i in dic.keys():
    print(i)
for i in dic.values():
    print(i)
for i,j in dic.items():
    print(i,j)

dic['framework'] ="Django"
print(dic)
del dic['framework']
print(dic)
dic.update({'framework':"Django"})
print(dic)
dic.pop('framework')
print(dic)

new = dict(name = "masud",age=25)
print(new)
new.clear()
print(new)
