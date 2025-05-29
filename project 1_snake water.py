'''
1 for snake
-1 for water
0 for gun
'''
import random

while True:             # it is used to run gamme in a loop
    computer = random.choice([0,-1,1])
    youch = input("enter your choice").lower()
    dic = {
        "s": 1,
        "w": -1,
        "g": 0,
        }
    reversedic={1: "snake",
                -1: "water",
                0: "gun",
    }
    you=dic[youch]
    print(f"You chose {reversedic[you]} \n and computer chose {reversedic[computer]}")
    if (computer == you):
        print("draw")
    elif(computer == -1 and you == 1):
        print("you won!")
    elif(computer== -1 and you == 0):
        print("computer won")
    elif(computer== 0 and you == 1):
        print("computer won")
    elif(computer== 0 and you == -1):
        print("you won")
    elif(computer== 1 and you == -1):
        print("computer won")
    elif(computer== 1 and you == 0):
        print("you won")
    else:
        print("someyhing went wrong!")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != "y":
        print("Game over. GG! 🎮")
        break
    print("\n--- Next Round ---\n")