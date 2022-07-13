#Import the random and time functions
import random
import time

#Prompt the user 
print('Hey! Wanna play rock paper scissors!?')

#A variable to control how the function bellow will work in different scenarios and another to control the loop.
prompt_switch=0
user_perm=True

#A function that will check the users input and respond appropriately.
def yes_no():
    #import these two variables into the function.
    global prompt_switch
    global user_perm
    #Lists that allow for more variation in possible answers a user can enter.
    yes_list=('YES','SURE','YEAH','READ','Y')
    no_list=('NO','NAH','N')
    check=False
    #While we haven't been given the a (valid) answer, ask the user to answer "Yes or no?"
    while check!=True:
        print('Yes or no?')
        answer=input()
        #If the user answers yes, set the check to be true and break the loop.
        if answer.upper() in yes_list:
            check=True
        #If the answer is no and we're not in the loop, close the script.
        elif answer.upper() in no_list:
            if prompt_switch==0:
                print ('Oh, okay, cya!')
                exit()
            #And if we are in the loop, break this one and the larger one it's in.
            else:
                print("Okay, this was fun, so come back when you're ready for more")
                check=True
                user_perm=False
        #If the answer we get is invalid, restart and ask them to say either "Yes or no?"
        else:
            check=False

#Use this function to prompt the user as they're introducing the game to them.
yes_no()
print ("Okay, let's go!")
print('When I say scissors, type in your answer!')
print('Ready?')
yes_no()

#Set up the scores so that it can be kept track of
user_score=0
computer_score=0

#While the computer still has the users permission to continue.
while user_perm==True:
    #Switch the functionality of the function so it works in loops and begin the game
    prompt_switch=1
    time.sleep(0.5)
    print('Okay!')
    time.sleep(0.5)
    print ('Rock')
    time.sleep(1)
    print('Paper')
    time.sleep(1)
    print('Scissors!')
    time.sleep(1)
    #Users answer is taken in
    user_choice=input()
    #Pick a random answer and make it the computer selection
    answer_list=('Rock','Paper','Scissors')
    computer_choice= random.choice(answer_list)
    #New function will assign a value depending on the answer which will allow for the game to be played.
    def assign_val(choice):
        #Variations of ways to type each valid response
        rock_list=('Rock','rock','r')
        paper_list=('Paper','paper','p')
        scissor_list=('Scissors','scissors','s')
        #If rock, the value returned will be 2
        if choice in rock_list:
            return 2
        #If paper, the value returned will be 6
        elif choice in paper_list:
            return 6
        #If scissors, the value returned will be -4
        elif choice in scissor_list:
            return -4
        #If none of these have been entered, a string, "Invalid" Will be returned
        else:
            return "Invalid"

    #Give both the user and computer's answers the correct value(using the assign_val function)
    user_choice_value= assign_val(user_choice)
    computer_choice_value= assign_val(computer_choice)

    #If the function returns as "Invalid" on the user end, prompt them repeatedly until they answer correctly
    while user_choice_value=="Invalid":
        print("It seems you entered something that isn't valid in this game, try entering rock, paper or scissors")
        user_choice=input()
        user_choice_value= assign_val(user_choice)

    #We determine who won by creating two results, created by dividing the choices by each other in both ways
    result1=computer_choice_value/user_choice_value
    result2=user_choice_value/computer_choice_value

    #Now we print what the computer chose so that the user can see.
    print (computer_choice)
    time.sleep(1)

    #If both values are the same then it's obviously a draw
    if user_choice_value==computer_choice_value:
        print("Tied, dang")
    #If the computers value divided by the user value is larger than the opposite, the computer has won.
    elif result1 > result2:
        print ('I Win!')
        #Increase the computers score
        computer_score+= 1
    #Likewise, if the users value divided by the computers value is larger than the opposite, they've won this round
    elif result2 > result1:
        print('You win!')
        #Increase the users score
        user_score+= 1

    time.sleep(1)
    print ("Sooo, it looks like...")
    time.sleep(2)
    #Print out the scores in ways that vary depending on score
    if user_score > computer_score:
        print (f"You're currently winning {user_score}-{computer_score} :(")
    elif computer_score > user_score:
        print (f"I'm currently winning {computer_score}-{user_score} :D")
    else:
        print (f"We're currently tied up at {computer_score}-{computer_score}, we should keep going and find a winner")

    time.sleep(1)
    #Prompt the user to do another round(using the switched up yes_no function)     
    print('Wanna go again!?')

    yes_no()


    
