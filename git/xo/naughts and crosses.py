import random

print ("Hello, wanna play naughts and crosses against me?")
print ("I'm not very good, but it could be fun :)")

yes_list=('Yes','yes','YES','yEs','yeS','YEs','yES')

no_list=('No','no','NO','nO')

ans_check= False

while ans_check!=True:
    print ("Yes or no?")
    request_ans=input()
    if request_ans in yes_list:
        ans_check=True
    elif request_ans in no_list:
        print ('Oh, okay ;-;')
        exit()
    else:
        ans_check=False

a={1:'-', 2:'-', 3:'-'}
b={1:'-', 2:'-', 3:'-'}
c={1:'-', 2:'-', 3:'-'}

rows=('a','b','c')

print("-|-|-")
print("-|-|-")
print("-|-|-")

print ("Okay, let's go :)")

char_check=False

while char_check==False:
    print ('Do you want to be x or o?')
    xoans=input()
    if xoans== 'X' or xoans=='x':
        user_character='X'
        computer_character='O'
        char_check=True
    elif xoans== 'O' or xoans=='o':
        user_character='O'
        computer_character='X'
        char_check=True
    else:
        char_check=False

print("Okay, I'll go first as ",computer_character,'then')

Availability={'a1':'-','a2':'-','a3':'-','b1':'-','b2':'-','b3':'-','c1':'-','c2':'-','c3':'-'}

Game=False

Rnd=0

print('Type the coordinates you want to place your character.')

def Gamecheck():
    diagonal_forward=c[1]+b[2]+a[3]
    diagonal_back=a[1]+b[2]+c[3]
    col1=a[1]+b[1]+c[1]
    col2=a[2]+b[2]+c[2]
    col3=a[3]+b[3]+c[3]
    OWin='OOO'
    XWin='XXX'
    global Availability
    avlen=len(Availability)
    global Game
    global draw_tag
    draw_tag=False
    rowA=""
    rowB=""
    rowC=""
    for i in list(a.values()):
        rowA=rowA+i
    for i in list(b.values()):
        rowB=rowB+i
    for i in list(c.values()):
        rowC=rowC+i
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
    elif avlen==0:
        print("It's a draw!")
        draw_tag=True
        Game=True
    else:
        Game=False

while Game==False:
    random_pick=random.choice(list(Availability.keys()))
    Availability.pop(random_pick)
    rslist=list(random_pick)
    rowsel=rslist[0]
    colsel=rslist[1]
    colsel=int(colsel)

    if rowsel== 'a':
        a[colsel]=computer_character
    elif rowsel== 'b':
        b[colsel]=computer_character
    elif rowsel== 'c':
        c[colsel]=computer_character
        
    print(a[1]+'|'+a[2]+'|'+a[3])
    print(b[1]+'|'+b[2]+'|'+b[3])
    print(c[1]+'|'+c[2]+'|'+c[3])

    Gamecheck()

    if Game==True:
        if draw_tag==False:
            print('Yay! I won!')
        else:
            print("-------------")
    else:
        if Rnd == 0:
            print ('For example, I just placed my piece on ',random_pick)
        else:
            print('There we go,')

        avlen=len(Availability)
            
        print ("Your turn now!")
        user_pick=input()

        while user_pick not in Availability:
            print('Oops! That spot is already filled, try again!')
            user_pick=input()

        Availability.pop(user_pick)
        ulist=list(user_pick)
        rowu= ulist[0]
        colu= ulist[1]
        colu=int(colu)

        if rowu== 'a':
            a[colu]=user_character
        elif rowu== 'b':
            b[colu]=user_character
        elif rowu== 'c':
            c[colu]=user_character

        Rnd+=1

        print(a[1]+'|'+a[2]+'|'+a[3])
        print(b[1]+'|'+b[2]+'|'+b[3])
        print(c[1]+'|'+c[2]+'|'+c[3])
        
        Gamecheck()

        if Game==True:
            print("Looks like you won")
            print('--------------------')
        else:
            print('Hmm, okay...')

print('Game over')

    






































    
