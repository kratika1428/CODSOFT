import random
choose=['Rock','Paper','Scissor']
'''rock v/s paper ---> paper wins
rock v/s scissor ---> rock wins
paper v/s scissor ---> scissor wins'''
while True:
    countC=0
    countU=0
    print("Do you want to play game:")
    userchoice=int(input("1. Yes! Lets play\n 2. No/Exit\n Enter your choice:"))
    if userchoice==1:
        for i in range(1,6):
            userinput=int(input("1.Rock\n 2.Paper\n 3.Scissor\n Enter your choice: "))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Paper"
            elif userinput==3:
                uchoice="Scissor"
            else:
                uchoice="Invalid input"
            Cchoice=random.choice(choose)
            print("You chosed ", uchoice)
            print("Computer chosed", Cchoice)
            if Cchoice==uchoice:
                print("Game draw")
                countC+=1
                countU+=1
            elif (Cchoice=='Rock' and uchoice=='Paper')or(Cchoice=='Scissor' and uchoice=='Rock')or(Cchoice=='Paper' and uchoice=='Scissor'):
                print("You win this round")
                countU+=1
            elif (Cchoice=='Paper' and uchoice=='Rock')or(Cchoice=='Rock' and uchoice=='Scissor')or(Cchoice=='Scissor' and uchoice=='Paper'):
                print("Computer win this round")
                countC+=1
            else:
                print("Invalid Choice")
        print("Total score")
        if countU>countC:
            print("Your score",countU)
            print("Computer score",countC)
            print("You win")
        elif countC>countU:
            print("Your score",countU)
            print("Computer score",countC)
            print("Computer wins")
        else:
            print("Your score",countU)
            print("Computer score",countC)
            print("Game draw")
    else:
        print("Game ends")
        break
    print("Game over!")
