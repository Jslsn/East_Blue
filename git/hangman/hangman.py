import random

#Greet the player
print ("let's play a game where you guess the letters in the word I'm thinking of!")

#Open a file full of words and turn each line into an item into a list before picking a random item from said list.
f=open("sowpods.txt","r")
fill=list(f)
word=random.choice(fill)

#Create a false-set boolean called Game_State and an empty dictionary called aid.
Game_state=False
aid={}
#Aid is the bars that inform the user which letters they have, it is created initially by going through the word
#and creating an underscore for each letter(The underscore is the value in the dictionary) and if the letter already
#exists in the keys, it will change the key for each repetition of the letter by adding a $ sign at the end.
for x in (word):
    if x in aid.keys():
        while x in aid.keys():
            x=x+"$"
            if x not in aid.keys():
                aid[x]="_"
                break
    else:
        aid[x]="_"

#New string
drow=""

#Clean up aid by removing the \n that will inevitably appear in the key.
del aid[str('\n')]
#Inform the user of the words letter count before printing the values of the word list, which at this point should
#just be a bunch of underscores.
print(f'there are {len(word)} letters in my word')
for i in (aid.values()):
    drow=drow+i
print(drow)

#These are all variables containing strings that can make a hanging man.
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

#This variable will determine which of the created strings will print.
stage=0

#While the user hasn't won, we start by resetting the drow variable and creating the guess variable with a word value
while Game_state==False:
    guess="blank"
    drow=""
    #Reason being that here, it will set off a loop that won't stop unless the user only enters a single letter
    while len(guess)>1:
        guess=input("guess the letters in my word! \n")
    #If the guess is in the word list, it will inform them and update the aid variable.
    if guess.upper()in word.upper():
        print("You got one of the letters!")
        aid[guess.upper()]=guess.upper()
        #This will fill in the potential dollar marked repeats.
        for x in aid:
            laid=list(x)
            if guess.upper() in laid:
                aid[x]=guess.upper()
        #If aid makes a complete word, the gamestate changes and the user is congratulated.
        if "_" not in aid.values():
            print("You got the word")
            Game_state=True
        #Refill drow and print it.
        for i in (aid.values()):
            drow=drow+i
        print(drow)
        if "_" not in aid.values():
            print("You got the word")
            Game_state=True
    #If the user got the answer wrong, we continue, we refill drow and reprint it for convenience sake, and increase
    #the value of stage.
    else:
        print("nope")
        for i in (aid.values()):
            drow=drow+i
        print(drow)
        stage+=1

    #From whatever happened before, we print the current state of the hangman depending on the value of stage.       
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
    #Once the user get's to 9, we print out the final state of the hangman, inform them of their loss before revealing
    #the word and ending the game by changing the game state.
    elif stage==9:
        print (pol7)
        print (plat)
        print("You ran out of lives!")
        print (f'the word was {word}!')
        Game_state=True


