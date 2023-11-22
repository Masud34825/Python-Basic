import datetime

print("Print Full Date time: ",datetime.datetime.now())
x = datetime.datetime.now()

print("Full Year is: ",x.strftime("%Y"))
print("Short Year is: ",x.strftime("%y"))
print("Miniute is: ",x.strftime("%M"))
print("Hour is: ",x.strftime("%H"))
print("Month is: ",x.strftime("%h"))

