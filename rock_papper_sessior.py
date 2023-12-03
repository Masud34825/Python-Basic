import random
l =["rock","paper","sessior"]
userCount =0
computerCount =0
while(True):
    
    userInput=int(input('''
                        Do you Want To Play Game:
                        Press 1 for Yes
                        press 2 for Exit                        
                        '''))
    
    if(userInput == 1):
        for i in range(1,6):
            userChoice = int(input('''
                            Your Choice to select:
                            Press 1 for Rock
                            press 2 for Paper
                            press 3 for Sessior                                     
                                '''))
            
            computerChoice = random.choice(l) 
                       
            if (userChoice == 1):
                userChoice = "rock"
            elif(userChoice==2):
                userChoice = "paper"
            else:
                userChoice ="sessior"
                
            if(userChoice == computerChoice):
                print("Match Drawn ")
                print("You Choice- ",userChoice)
                print("Computer Choice- ",computerChoice)
                userCount = userCount +1
                computerCount = computerCount+1
            elif( (userChoice == "rock" and computerChoice == "sessior") or (userChoice == "paper" and computerChoice == "rock") or (userChoice == "sessior" and computerChoice == "paper") ):
                print("You Win")
                print("You Choice- ",userChoice)
                print("Computer Choice- ",computerChoice)
                userCount = userCount +1
            else:
                print("Computer Win")
                print("You Choice- ",userChoice)
                print("Computer Choice- ",computerChoice)
                computerCount = computerCount+1
                
        print("----------xxxxxxxxxxx------------")
        print("----------xxxxxxxxxxx------------")
        
        if(computerCount == userCount):
           print("Final Reasult Match Drawn!")
           print("Your Final Score - ",userCount)
           print("Computer Final Score- ",computerCount) 
        elif(computerCount > userCount):
            print("Final Reasult Computer Win!")
            print("Your Final Score - ",userCount)
            print("Computer Final Score- ",computerCount) 
        else:
            print("Final Reasult You Win!")
            print("Your Final Score - ",userCount)
            print("Computer Final Score- ",computerCount) 
            
    else:
        break
    