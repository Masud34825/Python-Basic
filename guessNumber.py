import random

computerNumber = random.randint(1,20)

userNumber = int(input("Enter Your Number Between 1 to 20:--"))

if(computerNumber > userNumber):
    print("Computer Number is:-",computerNumber)
    print("Your Number is too low then computer Number",userNumber)
elif( userNumber > computerNumber):
    print("Computer Number is:-",computerNumber)
    print("Your Number is too Higher then computer Number",userNumber)
else:
    print("Computer Number is:-",computerNumber)
    print("Match Draw your input Computer number is same",userNumber)