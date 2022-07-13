import random

#Introduction
print ("Hello, wanna play naughts and crosses against me?")
print ("I'm not very good, but it could be fun :)")

#A somewhat excessive list anticipating various ways the user may answer Yes or No.
yes_list=('YES','Y')

no_list=('NO','N')

#A loop to avoid anything wonky happening if the user answers in a way the script isn't equipped to deal with.

#Boolean for the loop.
ans_check= False

#While the boolean is false.
while ans_check!=True:
    #Ask the user to answer yes or no and provide an input.
    print ("Yes or no?")
    request_ans=input()
    #If they answered yes, we can leave the loop and carry on with the script.
    if request_ans.upper() in yes_list:
        ans_check=True
    #If they answered no, the script closes.
    elif request_ans.upper() in no_list:
        print ('Oh, okay ;-;')
        exit()
    #If anything else is answered, loop back; printing "Yes or no" Again should nudge them to enter something valid.
    else:
        ans_check=False

#Each row is a dictionary so they can be refered to in code in a similar way as in game.
a={1:'-', 2:'-', 3:'-'}
b={1:'-', 2:'-', 3:'-'}
c={1:'-', 2:'-', 3:'-'}

rows=('a','b','c')

#Prints what the grid will look like to introduce the player to their board.
print("-|-|-")
print("-|-|-")
print("-|-|-")

print ("Okay, let's go :)")

#Another loop like the one earlier, but this time with allowing the user to choose their piece.
char_check=False

while char_check==False:
    #Prompting the user into filling a variable that will affect the results of other variables.
    print ('Do you want to be x or o?')
    xoans=input()
    #If the users input is x, it sets the users piece to be X and the scripts to O.
    if xoans== 'X' or xoans=='x':
        user_character='X'
        computer_character='O'
        char_check=True
    #If the users input is o, it sets the users piece to be X and the scripts to X.
    elif xoans== 'O' or xoans=='o':
        user_character='O'
        computer_character='X'
        char_check=True
    #Otherwise we loop back, prompting them to re-enter either x or o.
    else:
        char_check=False

#The script always makes the first move and here it just confirms that the users input has been received.

print("Okay, I'll go first as ",computer_character,'then')

#This availability variable is important, it will stop either of the players from making moves where they cannot.
Availability={'a1':'-','a2':'-','a3':'-','b1':'-','b2':'-','b3':'-','c1':'-','c2':'-','c3':'-'}

#Game is essentially going to be a way to finish the game once certain requirements are fulfilled.
Game=False

#This is for when we get into the game loop, it affects dialogue later that helps introduce the player into the game.
Rnd=0

#This is the start of the introduction to the game that will teach the user how to interact with the board they see.
print('Type the coordinates you want to place your character.')

#An inputless function that will be called upon whenever a check of the board/gamestate needs to be checked.
def Gamecheck():
    #These 5 variables pull the characters on the potential winning lines into a string.
    diagonal_forward=c[1]+b[2]+a[3]
    diagonal_back=a[1]+b[2]+c[3]
    col1=a[1]+b[1]+c[1]
    col2=a[2]+b[2]+c[2]
    col3=a[3]+b[3]+c[3]
    #The variables will be compaired to these two strings to determine if a winning state has been reached.
    OWin='OOO'
    XWin='XXX'
    #Bringing in a few global variables to be affected by the results of these checks.
    #Also creating a variable that keeps an eye on the available spaces so that a draw can eventually be detected.
    global Availability
    avlen=len(Availability)
    global Game
    #Creating a new draw_tag variable that is global
    global draw_tag
    draw_tag=False
    #Creating a few blank variables and filling them in with the values of each row to be compared/checked.
    rowA=""
    rowB=""
    rowC=""
    for i in list(a.values()):
        rowA=rowA+i
    for i in list(b.values()):
        rowB=rowB+i
    for i in list(c.values()):
        rowC=rowC+i
    #If any of the potential winning line variables are all X or all O, set the game as finished.
    if rowA== XWin or rowA==OWin:
        print('win on rowA')
        Game=True
    elif rowB == XWin or rowB==OWin:
        print('win on rowB')
        Game=True
    elif rowC == XWin or rowC==OWin:
        print('win on rowC')
        Game=True
    elif col1 == XWin or col1==OWin:
        print('win on column 1')
        Game=True
    elif col2 == XWin or col2==OWin:
        print('win on column 2')
        Game=True
    elif col3 == XWin or col3==OWin:
        print('win on column 3')
        Game=True
    elif diagonal_forward== XWin or diagonal_forward==OWin:
        print('win diagonally forward')
        Game=True
    elif diagonal_back== XWin or diagonal_back==OWin:
        print('win diagonally backward')
        Game=True
    #If there are no available spots on the grid, the game is a draw and will end.
    elif avlen==0:
        print("It's a draw!")
        draw_tag=True
        Game=True
    #Otherwise, the game goes on
    else:
        Game=False

#While the game has not ended.
while Game==False:
    #The computer picks a space that's available on the grid.
    random_pick=random.choice(list(Availability.keys()))
    #Then the space that has just been selected will be removed from the potential future moves.
    Availability.pop(random_pick)
    #We create 3 variables, the two important ones seperately identify the row and column the selected belongs to.
    rslist=list(random_pick)
    rowsel=rslist[0]
    colsel=rslist[1]
    colsel=int(colsel)

    #In whichever row the selected belongs to, place the computers character into column of the selected.
    if rowsel== 'a':
        a[colsel]=computer_character
    elif rowsel== 'b':
        b[colsel]=computer_character
    elif rowsel== 'c':
        c[colsel]=computer_character

    #Print out the changed state of the grid
    print(a[1]+'|'+a[2]+'|'+a[3])
    print(b[1]+'|'+b[2]+'|'+b[3])
    print(c[1]+'|'+c[2]+'|'+c[3])

    #Check the state of the game.
    Gamecheck()

    #If the game is done at this point and there's no draw, the computer made the winning move and can celebrate.
    if Game==True:
        if draw_tag==False:
            print('Yay! I won!')
            print("-------------")
        #If a draw is detected, nothing is said since the line for a draw is already said in the function.    
        else:
            print("-------------")
    #Otherwise, we continue with the round.
    else:
        #If this is the first round, introduce the player to the game by telling them how to affect the board.
        if Rnd == 0:
            print ('For example, I just placed my piece on ',random_pick)
        #Else, just give a simple message of confirmation.
        else:
            print('There we go,')
        
        avlen=len(Availability)

        #Prompt the user into entering a command.
        print ("Your turn now!")
        user_pick=input()

        #If the spot the user picked is not available, repeatedly give them the opportunity to retry.
        while user_pick not in Availability:
            print('Oops! That spot is already filled, try again!')
            user_pick=input()

        #Get the users selected out of the available spots and create a variable that identifies it's row and column
        Availability.pop(user_pick)
        ulist=list(user_pick)
        rowu= ulist[0]
        colu= ulist[1]
        colu=int(colu)

        #In whatever row the user has selected, place their character in the column it belongs to.
        if rowu== 'a':
            a[colu]=user_character
        elif rowu== 'b':
            b[colu]=user_character
        elif rowu== 'c':
            c[colu]=user_character

        #Count up the round purely to stop the first round message from printing.
        Rnd+=1

        #Show the users changes to the grid.
        print(a[1]+'|'+a[2]+'|'+a[3])
        print(b[1]+'|'+b[2]+'|'+b[3])
        print(c[1]+'|'+c[2]+'|'+c[3])

        #Check the game
        Gamecheck()

        #If the game finishes at this point and there's no draw, the user made the winning move
        if Game==True:
            if draw_tag == False:
                print("Looks like you won")
                print('--------------------')
            #If there is a draw, don't say anything, the draw message has already been said
            else:
                print("-------------")
        #Otherwise, we loop back with a round closing message.
        else:
            print('Hmm, okay...')

#Whatever the result is, print that the game is over.
print('Game over')

    






































    
