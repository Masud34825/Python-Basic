l =[]
while(True):
    select = int(input('''
              Choice Your Options Below:-
              1) Press 1 For input Value To Queue 
              2) Press 2 For Delete Value To queue 
              3) Press 3 For Show all Value of queue 
              4) Press 4 For Show Front Value of queue 
              5) Press 5 For Show Rear/Last Value of queue 
              6) Press 6 For Exit the Programm 
              
              '''))
    if (select == 1 ):
        value = input("Enter Your Value:-")
        l.append(value)
        print("Your queue Now:-",l)
    elif (select == 2 ):
        if( len(l) > 0):
            l.pop(0)
            print("Your queue Now:-",l)
        else:
            print("Your queue Is Already Empty")
    elif ( select == 3 ):
          print("Your queue Now:- ",l)   
    elif ( select == 4 ):
          print("Your queue Front/First Element is:- ",l[0])   
    elif ( select == 5 ):
          print("Your queue Rear/Last Element is:- ",l[-1])   
    elif ( select == 6 ):
          break
    else:
        print("Invalid Choice Try Again")   
    
    