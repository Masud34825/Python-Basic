import os
w=open("demo.txt","w")
w.write("\nNew Line Added")
w.close()
f = open("demo.txt","r")
print(f.read())
f.close()

print(os.path.exists("demo.txt"))

# os.remove("demo.txt")  [Delete Any File]
# os.rmdir("demo") [Delete any empty folder]