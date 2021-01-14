while True:
    playerone = input("Choose your fighter playerone: ")
    playertwo = input("Choose your fighter plyaertwo: ")
 
    a= "scissor"
    b= "paper"
    c= "rock"

    if playerone == a and playertwo == a:
        print("Draw")
    elif playerone == a and playertwo == b:
        print("Player One Win")
    elif playerone == a and playertwo == c:
        print("Player Two wins")
    elif playerone == b and playertwo == a:
        print("player two Wins")
    elif playerone == b and playertwo == b:
        print("draw")
    elif playerone == b and playertwo == c:
        print("player one win")
    elif playerone == c and playertwo == a:
        print("Player one win")
    elif playerone == c and playertwo == b:
        print("Player two wins")
    elif playerone == c and playertwo == c:
        print("draw")

    ans = input("Want to replay? ")
    if ans == "yes":
        continue
    else:
        break