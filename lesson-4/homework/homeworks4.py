import random
play=True
while play:
    num=random.randint(1,100)
    found=False
    i=1
    while not found and i<=10:
        guess=int(input("guess the number: "))
        if guess>num:
            print("Too high")
        elif guess<num:
            print("Too low")
        else:
            print("You guessed it right!")
            found=True
            play=False
        i=i+1
    if not found:
        a=input("You lost. Want to play again? ")
        if a in ['Y', 'YES', 'y', 'yes', 'ok']:
            play=True
        
