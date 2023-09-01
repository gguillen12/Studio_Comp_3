from getpass import getpass as input

print("Rock, Paper,Scissors!")
print("Press r for rock, s for scissors, and p for paper. Then press ENTER.")
print()

counterOne = 1
counterTwo = 1
while True:
    playerOne = input("Player One, select move.")
    playerTwo = input("Player Two, select move.")
    if playerOne == "p" and playerTwo == "r":
        print()
        print("Paper covers rock! Player one wins!", counterOne, "point")
        counterOne += 1
        if counterOne != 4:
            continue
        else:
            print("Player One wins the match!")
            break
            exit()
    elif playerTwo == "p" and playerOne == "r":
        print()
        print("Paper covers rock! Player two wins!", counterTwo, "point.")
        counterTwo += 1
        if counterTwo != 4:
            continue
        else:
            print("Player Two wins the match!")
            break
            exit()

    elif playerOne == "s" and playerTwo == "p":
        print()
        print("Scissors cuts paper! Player one wins!", counterOne, "point.")
        counterOne += 1
        if counterOne != 4:
            continue
        else:
            print("Player One wins the match!")
            break
            exit()
    elif playerTwo == "s" and playerOne == "p":
        print()
        print("Scissors cuts paper! Player two wins!", counterTwo, "point.")
        counterTwo += 1
        if counterTwo != 4:
            continue
        else:
            print("Player One wins the match!")
            break
            exit()

    elif playerOne == "r" and playerTwo == "s":
        print()
        print("Rock beats scissors! Player one wins!", counterOne, "point.")
        counterOne += 1
        if counterOne != 4:
            continue
        else:
            print("Player One wins the match!")
            break
            exit()
    elif playerTwo == "r" and playerOne == "s":
        print()
        print("Rock beats scissors! Player two wins!", counterTwo, "point")
        counterTwo += 1
        if counterTwo != 4:
            continue
        else:
            print("Player Two wins the match!")
            break
            exit()

    elif playerOne != "r" and playerOne != "p" and playerOne != "s" and playerTwo != "r" and playerTwo != "p" and playerTwo != "s":
        print("Invalid Key Entry for both players. Please Try again.")
        if counterOne != 4 and counterTwo != 4:
            print()
            continue
        else:
            break
            exit()

    elif playerOne != "r" and playerOne != "p" and playerOne != "s":
        print("Invalid Key Entry for player one. Please try again.")
        if counterOne != 4 and counterTwo != 4:
            print()
            continue
        else:
            break
            exit()
    elif playerTwo != "r" and playerTwo != "p" and playerTwo != "s":
        print("Invalid Key Entry for player two. Please try again.")
        if counterOne != 4 and counterTwo != 4:
            print()
            continue
        else:
            break
            exit()
    elif playerOne == "s" and playerTwo == "s":
        print("It's a draw!")
        if counterOne != 4 and counterTwo != 4:
            print()
            continue
        else:
            break
            exit()

    elif playerOne == "r" and playerTwo == "r":
        print("It's a draw!")
        if counterOne != 4 and counterTwo != 4:
            print()
            continue
        else:
            break
            exit()

    elif playerOne == "p" and playerTwo == "p":
        print("It's a draw!")
        if counterOne != 4 and counterTwo != 4:
            print()
            continue
        else:
            break
            exit()
else:
    print("Good game! Would you like to play again?")
