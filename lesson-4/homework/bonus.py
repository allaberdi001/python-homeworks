import random
choices=["rock","paper","scissors"]
u=0
c=0
for i in range(5):
    pc_choice=random.choice(choices)
    user_choice=input("your choice: ")
    if pc_choice=="rock" and user_choice=="paper":
        u=u+1
        print("user wins")
    elif pc_choice=="rock" and user_choice=="scissors":
        c=c+1
        print("computer wins")
    elif pc_choice=="paper" and user_choice=="rock":
        c=c+1
        print("computer wins")
    elif pc_choice=="paper" and user_choice=="scissors":
        u=u+1
        print("user wins")
    elif pc_choice=="scissors" and user_choice=="paper":
        c=c+1
        print("computer wins")
    elif pc_choice=="scissors" and user_choice=="rock":
        u=u+1
        print("user wins")
    elif pc_choice==user_choice:
        print("draw!!")
if c>u:
    print("Computer wins the match")
elif u>c:
    print("user wins the match")
else:
    print("The match was Draw!!")
