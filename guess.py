import random

while True:
    guessnum = random.randint(1,10)
    print("Guess the number from 1 to 9: ")
    while True:
        answer = int(input("Please input your guess"))
        if answer > 9:
            print("9  is the highest number")
        else:
            if answer == guessnum:
                print(answer, " You Exactly Right")
                break
            elif answer >= guessnum:
                print(answer, "your Guess is bit to high")
            elif answer <= guessnum:
                print(answer, "Your Guess is a bit lower")
    
    replay=input("Want to Replay the game?")
    if replay == "yes":
        continue
    else:
        break
