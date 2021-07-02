import random
def devinfo():
    print("Developer Informaion:\nRohan Choudhary 1803211042\nTarang Agrawal 1803211054")
#Rock Paper Scissiors Game
def rock_paper_scissor():
    print("Welcome to Rock Paper Scissors\nThis game consists of two modes:\n3 rounds\n5 rounds\n")
    x=int(input("Enter:\n1. for 3 round game\n2. for 5 round game\n3. to exit\n"))
    if x==1:#Program for 3 round game
        c=0#Points of Computer
        p=0#Points of Player
        i=1
        while i<=3:#For 3 rounds
            y=int(input("Enter:\n1. for Rock\n2. for Paper\n3. for Scissors\n"))#Choice of Player
            z=random.randint(1,3)#Choice of computer
            if y==1:
                if z==1:#User and Computer both has Rock
                    print("You both had Rock")
                elif z==2:#User has rock and computer has paper
                    print("Oops! Computer had Paper")
                    c+=1
                elif z==3:#User has rock and computer has scissors
                    print("Good! Computer had Scissors")
                    p+=1
            elif y==2:
                if z==1:#User has paper and computer has rock
                    print("Good! Computer had Rock")
                    p+=1
                elif z==2:#User and Computer both have Paper
                    print("You both had Paper")
                elif z==3:#User has paper and computer has scissors
                    print("Oops! Computer had Scissors")
                    c+=1
            elif y==3:
                if z==1:#User has Scissors and computer has Rock
                    print("Oops! Computer had rock")
                    c+=1
                elif z==2:#User has Scissor and computer has Paper
                    print("Good! Computer had Paper")
                    p+=1
                elif z==3:#User and computer both has Scissors
                    print("You both had Scissors")
            i+=1
        print("Final Points\You-{}  Computer-{}".format(p,c))
        if p>c:
            print("You Won!")
        elif p<c:
            print("Sorry! You Lost.")
        e=input("Enter e to Exit")
        if e=="e":
            rock_paper_scissor()
    elif x==2:#Program for 5 round game
        c=0#Points of Computer
        p=0#Points of Player
        i=1
        while i<=5:#For 5 rounds
            y=int(input("Enter:\n1. for Rock\n2. for Paper\n3. for Scissors"))#Choice of Player
            z=random.randint(1,3)#Choice of computer
            if y==1:
                if z==1:#User and Computer both has Rock
                    print("You both had Rock")
                elif z==2:#User has rock and computer has paper
                    print("Oops! Computer had Paper")
                    c+=1
                elif z==3:#User has rock and computer has scissors
                    print("Good! Computer had Scissors")
                    p+=1
            elif y==2:
                if z==1:#User has paper and computer has rock
                    print("Good! Computer had Rock")
                    p+=1
                elif z==2:#User and Computer both have Paper
                    print("You both had Paper")
                elif z==3:#User has paper and computer has scissors
                    print("Oops! Computer had Scissors")
                    c+=1
            elif y==3:
                if z==1:#User has Scissors and computer has Rock
                    print("Oops! Computer had rock")
                    c+=1
                elif z==2:#User has Scissor and computer has Paper
                    print("Good! Computer had Paper")
                    p+=1
                elif z==3:#User and computer both has Scissors
                    print("You and Computer both had Scissors")
            i+=1
        print("Final Points\nYou-{}  Computer-{}".format(p,c))
        if p>c:
            print("You Won!")
        elif p<c:
            print("Sorry! You Lost.")
        e=input("Enter e to exit")
        if e=="e":
            rock_paper_scissor()
    elif x==3:
        games()
    
                
#Guess The Number Game
def  choose_a_number():
    print("Welcome!")
    #The Game will run until user press e for exit
    p="y"
    while p=="y":
        #Asking user to choose a level from 1 to 5
        y=int(input("Select Level\n1.Beginner\n2.Easy\n3.Medium\n4.Hard\n5.Expert\n6.Back to games\n"))
        if y==1:
            print("Instructions:\nYou have to guess a number between 1 to 10 in 4 guesses")
            z=random.randint(1,10)
            c=1
            while c!=5:
                u=int(input("Guess a number"))#getting a number from user
                if u<z:
                    print("Low")
                elif u>z:
                    print("High")
                elif u==z:
                    print("Yeah! You got it right in {} attempts".format(c))
                    break
                c+=1
            else:
                print("Oops! The number of tries are over.")
        elif y==2:
            print("Instructions:\nYou have to guess a number between 1 to 20 in 6 guesses")
            z=random.randint(1,20)
            c=1
            while c!=7:
                u=int(input("Guess a number"))#getting a number from user
                if u<z:
                    print("Low")
                elif u>z:
                    print("High")
                elif u==z:
                    print("Yeah! You got it right in {} attempts".format(c))
                    break
                c+=1
            else:
                print("Oops! The number of tries are over.")
        elif y==3:
            print("Instructions:\nYou have to guess a number between 1 to 50 in 8 guesses")
            z=random.randint(1,50)
            c=1
            while c!=9:
                u=int(input("Guess a number"))#getting a number from user
                if u<z:
                    print("Low")
                elif u>z:
                    print("High")
                elif u==z:
                    print("Yeah! You got it right in {} attempts".format(c))
                    break
                c+=1
            else:
                print("Oops! The number of tries are over.")
        elif y==4:
            print("Instructions:\nYou have to guess a number between 1 to 50 in 6 guesses")
            z=random.randint(1,50)
            c=1
            while c!=13:
                u=int(input("Guess a number"))#getting a number from user
                if u<z:
                    print("Low")
                elif u>z:
                    print("High")
                elif u==z:
                    print("Yeah! You got it right in {} attempts".format(c))
                    break
                c+=1
            else:
                print("Oops! The number of tries are over.")
        elif y==5:
            print("Instructions:\nYou have to guess a number between 1 to 100 in 8 guesses")
            z=random.randint(1,100)
            c=1
            while c!=9:
                u=int(input("Guess the number"))#Getting a number from user
                if u<z:
                    print("Low")
                elif u>z:
                    print("High")
                elif u==z:
                    print("Yeah! You got it right in {} attempts".format(c))
                    break
                c+=1
            else:
                print("Oops! The number of tries are over.")
        elif y==6:
            games()
            break
        p=input("To play again enter y\n To exit enter e")
    else:
        games()
#Rolling a dice game
def roll_a_dice():
    f="y"
    while f=="y":
        e=random.randint(1,6)
        print("you got",e)
        f=input("For rolling again enter y To Exit enter m\n")
    else:
        games()
#Going to games Arcade
def games():
    d=int(input("What whould like to play:\nEnter\n1. For Guess The Number\n2. For Rock Paper Scissor\n3. For Rolling a dice\nFor main menu enter 4\n"))
    if d==1:
        choose_a_number()
    elif d==2:
        rock_paper_scissor()
    elif d==3:
        roll_a_dice()
    else:
        main()
def main():#To call main menu again and again
    print("Welcome to the Game Arcade")
    n=int(input("Enter:\n1.For Games\n2.For Developer Information\n"))
    if n==2:
        devinfo()
        print()
        main()
    elif n==1:
        games()
main()

