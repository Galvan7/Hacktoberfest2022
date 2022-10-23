import random 
#from random import randint      for specific only

def game(p1,you):
    if p1=='R':
        if you=='S':
            return False
        elif you=='P':
            return True
        else:
            return None
    if p1=='P':
        if you=='R':
            return False
        elif you=='S':
            return True
        else:
            return None
    if p1=='S':
        if you=='P':
            return False
        elif you=='R':
            return True
        else:
            return None


rand=random.randint(1,3)
if rand==1:
    p1='R'
elif rand==2:
    p1='P'
else :
    p1='S'

you=input("YOUR TURN : ROCK(R) PAPER(P) OR SCISSORS(S) ")
a=game(p1,you)
print(f"YOU HAVE PICKED {you} AND COMPUTER HAS PICKED {p1}")
if(a==None):
    print("DAMN!ITS A TIE GO AGAIN ")
elif (a==True):
    print("YOU HAVE WON ! ")
else:
    print("HAHA YOU LOST! ")
