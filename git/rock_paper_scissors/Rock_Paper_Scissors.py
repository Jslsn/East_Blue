import random

RPS=('Rock','Paper','Scissors')

print('Hey! Wanna play rock paper scissors!?')

yes_list=('Yes','yes','YES','yEs','yeS','YEs','yES','Sure','sure','yeah','Yeah','Ready','ready')

no_list=('No','no','NO','nO','Nah','nah')

answer_check=False

user_perm=True

def yes_no():
    global yes_list
    global no_list
    check=False
    while check!=True:
        print('Yes or no?')
        answer=input()
        if answer in yes_list:
            check=True
        elif answer in no_list:
            print ('Oh, okay, cya!')
            exit()
        else:
            check=False

yes_no()
print ("Okay, let's go!")
answer_list=('Rock','Paper','Scissors')
print('When I say scissors, type in your answer!')
print('Ready?')
yes_no()

user_score=0
computer_score=0

while user_perm==True:
    """
    while answer_check!=True:
        print('Yes or no?')
        user_answer=input()
        if user_answer in yes_list:
            answer_check=True
            user_perm=True
        elif user_answer in no_list:
            print ('Oh, okay, cya!')
            exit()
        else:
            answer_check=False
    
    yes_no()
    print ("Okay, let's go!")
    answer_list=('Rock','Paper','Scissors')
    print('When I say scissors, type in your answer!')
    print('Ready?')
    yes_no()
    """


    print('Okay!')
    print ('Rock')
    print('Paper')
    print('Scissors!')
    user_choice=input()
    computer_choice= random.choice(answer_list)
    def assign_val(choice):
        rock_list=('Rock','rock')
        paper_list=('Paper','paper')
        scissor_list=('Scissors','scissors')
        if choice in rock_list:
            return 2
        elif choice in paper_list:
            return 6
        elif choice in scissor_list:
            return -4
        else:
            return "Invalid"
    
    user_choice_value= assign_val(user_choice)
    computer_choice_value= assign_val(computer_choice)

    while user_choice_value=="Invalid":
        print("It seems you entered something that isn't valid in this game, try entering rock, paper or scissors")
        user_choice=input()
        user_choice_value= assign_val(user_choice)

    result1=computer_choice_value/user_choice_value
    result2=user_choice_value/computer_choice_value

    print (computer_choice)
        
    if user_choice_value==computer_choice_value:
        print("Tied, dang")
        
    elif result1 > result2:
        print ('I Win!')
        computer_score+= 1
    elif result2 > result1:
        print('You win!')
        user_score+= 1
        
    if user_score > computer_score:
        print (f"You're currently winning {user_score}-{computer_score} :(")
    elif computer_score > user_score:
        print (f"I'm currently winning {computer_score}-{user_score} :D")
    else:
        print (f"We're currently tied up at {computer_score}-{computer_score}, we should keep going and find a winner")
        
    print('Wanna go again!?')

    yes_no()


    




#Try to play it in a loop so that the user can easily go again. Maybe keep score too?

