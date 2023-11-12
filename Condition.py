num = int(input("Enter Any Number to check Even Odd ?"))

if num%2==0:
    print("Even Number: ",num)
else:
    print("Odd Number: ",num)

num2 = eval(input("Enter Any Number to Check Grade ?"))

if(num2>=80 and num2< 101):
    print("Youre Grade is A+ :",num2)
elif(num2>=70 and num2< 80):
    print("Youre Grade is A :",num2)
elif(num2>=60 and num2< 70):
    print("Youre Grade is B :",num2)
elif(num2>=50 and num2< 60):
    print("Youre Grade is A+ :",num2)
elif(num2>=40 and num2< 50):
    print("Youre Grade is C :",num2)
elif(num2>=33 and num2< 40):
    print("Youre Grade is D :",num2)
else:
    print("You are Fail!")