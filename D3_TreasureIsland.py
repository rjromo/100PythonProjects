#Project for day 3

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")
direction = input("Left or Right?\n").lower()
if direction =='right':
    print("You chose 'Right' \nGameOver!")
else:
    print("You chose 'Left'")
    action = input('Choose between swim or wait\n').lower()
    if action == 'swim':
        print("You chose 'Swim' \nGameOver!")
    else:
        print("You chose 'Wait'")
        door = input('Which door \nRed, blue or yellow?\n').lower()
        if door == 'red' or door == 'blue':
            print("Game Over.")
        else:
            print("You win")