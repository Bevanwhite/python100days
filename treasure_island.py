print("Welcome to Treasure Island.Your mission is to find the treasure.")
left = input("left or right? \n").lower()
if(left == "left"):
    wait = input("swim or wait? \n").lower()
    if(wait == "wait"):
        which = input("Which door? (Red|Yellow|Blue) \n").lower()
        if(which == "Blue"):
            print("Eaten by beasts. Game Over.")
        elif(which == "yellow"):
            print("You Win")
        elif(which == "red"):
            print("Burned by fire. Game Over.")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.Game Over.") 
else:
    print("Fall into a hole. Game Over.")