"""
Let’s continue building Hangman. In the game of Hangman, a clue word is given
by the program that the player has to guess, letter by letter.
The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before
losing).
Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
write the logic that asks a player to guess a letter and displays letters 
in the clue word that were guessed correctly. For now, let the player guess
an infinite number of times until they get the entire word.
As a bonus, keep track of the letters the player guessed and display a
different message if the player tries to guess that letter again. 
Remember to stop the game when all the letters have been guessed correctly!
Don’t worry about choosing a word randomly or keeping track of the
number of guesses the player has remaining -
we will deal with those in a future exercise.

"""
import random

print ("let's play a game where you guess the letters in the word I'm thinking of!")

f=open("sowpods.txt","r")
fill=list(f)
word=random.choice(fill)
yuh=False
aid={}
for x in (word):
    if x in aid.keys():
        while x in aid.keys():
            x=x+"$"
            if x not in aid.keys():
                aid[x]="_"
                break
    else:
        aid[x]="_"
drow=""
del aid[str('\n')]
print(f'there are {len(word)} letters in my word')
for i in (aid.values()):
    drow=drow+i
print(drow)
plat="____|__"
pol="    |\n    |\n    |\n    |\n    |\n    |\n    |"
bar="    -----"
pol2="    |-----\n    |\n    |\n    |\n    |\n    |\n    |"

pol3="    |-----\n    |     |\n    |\n    |\n    |\n    |\n    |"
pol4="    |-----\n    |     |\n    |     0\n    |\n    |\n    |\n    |"
pol5="    |-----\n    |     |\n    |     0\n    |     |\n    |\n    |\n    |"
pol6="    |-----\n    |     |\n    |     0\n    |    -|-\n    |\n    |\n    |"
pol7="    |-----\n    |     |\n    |     0\n    |    -|-\n    |   _/ \_\n    |\n    |"

pol0="    |\n    |"
pol01="    |\n    |\n    |\n    |"


stage=0

while yuh==False:
    guess="shoop"
    drow=""
    while len(guess)>1:
        guess=input("guess the letters in my word! \n")
    if guess.upper()in word.upper():
        print("You got one of the letters!")
        aid[guess.upper()]=guess.upper()
        for x in aid:
            laid=list(x)
            if guess.upper() in laid:
                aid[x]=guess.upper()
        if "_" not in aid.values():
            print("You got the word")
            yuh=True
        for i in (aid.values()):
            drow=drow+i
        print(drow)
        if "_" not in aid.values():
            print("You got the word")
            yuh=True
    else:
        print("nope")
        for i in (aid.values()):
            drow=drow+i
        print(drow)
        stage+=1

          
    if stage==1:
        print (plat)

    elif stage==2:
        print (pol0)
        print (plat)
        
    elif stage==3:
        print (pol01)
        print (plat)

    elif stage==4:
        print (pol2)
        print (plat)

    elif stage==5:
        print (pol3)
        print (plat)

    elif stage==6:
        print (pol4)
        print (plat)

    elif stage==7:
        print (pol5)
        print (plat)

    elif stage==8:
        print (pol6)
        print (plat)
    elif stage==9:
        print (pol7)
        print (plat)
        print("You ran out of lives!")
        print (f'the word was {word}!')
        yuh=True

