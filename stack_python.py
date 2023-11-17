l =[]
while(True):
    select = int(input('''
              Choice Your Options Below:-
              1) Press 1 For input Value To Stack 
              2) Press 2 For Delete Value To Stack 
              3) Press 3 For Show all Value of Stack 
              4) Press 4 For Show Last Value of Stack 
              5) Press 5 For Exit the Programm 
              
              '''))
    if (select == 1 ):
        value = input("Enter Your Value:-")
        l.append(value)
        print("Your Stack Now:-",l)
    elif (select == 2 ):
        if( len(l) > 0):
            l.pop()
            print("Your Stack Now:-",l)
        else:
            print("Your Stack Is Already Empty")
    elif ( select == 3 ):
          print("Your Stack Now:- ",l)   
    elif ( select == 4 ):
          print("Your Stack Last Element is:- ",l[-1])   
    elif ( select == 5 ):
          break
    else:
        print("Invalid Choice Try Again")   
    
    