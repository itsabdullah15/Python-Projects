import random
print("Print s for snake , w for water , g for Gun: ")

choices = ('s','w','g')
a = random.choice(choices)
print(a)
score = 0
i=1

# while i<=10:
import random
print("you have 10 chances")
score=0
computer=0
chance=0
while(chance<10):
    n=int(input("enter your choice \n 0-snake \n 1-water \n 2-gun  \n"))
    chance=chance+1
    lst=["snake","water","gun"]
    choice=random.choice(lst)
    if choice =="snake":
        if n==0:
            print("its a tie")
            score=score+0
        elif n==1:
            print("you lost water snake drank you water")
            computer=computer+1
        else:
            print("you won sanke got shot")
            score=score+1
    elif choice=="water":
        if n==0:
            print("you won")
            score=score+1
        elif n==1:
            print("its a tie")
        else:
            print("you lost")
            computer=computer+1
    else:
        if n==0:
            print("you lost")
            computer =computer +1
        elif n==1:
            print("you won")
            score=score+1
        else:
            print("its a tie")
else:
    print("game over",computer,score)