# Project for day 4
import random

# rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''


# Paper
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''


# Scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

images = [rock, paper, scissors]

user = input(
    "What do you choose? \nType 0 for ROCK \nType 1 for PAPER \nType 2 for SCISSORS\n")

print("You choose: \n")
if user == 0:
    print(images[0])
elif user == 1:
    print(images[2])
elif user == 2:
    print(images[2])
    
computer = random.randint(0, 2)

if computer == 0 and user == 0:
    print('Computer choose: \nimages[0]\n\nTIE.')
elif computer == 0 and user == 1:
    print('Computer choose: \nimages[0]\n\nYou lose.')
elif computer == 0 and user == 2:
    print('Computer choose: \nimages[0]\n\nYou win.')
elif computer == 1 and user == 0:
    print('Computer choose: \nimages[1]\n\nYou lose.')
elif computer == 1 and user == 1:
    print('Computer choose: \nimages[1]\n\nTIE.')
elif computer == 1 and user == 2:
    print('Computer choose: \nimages[1]\n\nYou win.')
elif computer == 2 and user == 0:
    print('Computer choose: \nimages[2]\n\nYou win.')
elif computer == 2 and user == 1:
    print('Computer choose: \nimages[2]\n\nYou lose.')
elif computer == 2 and user == 2:
    print('Computer choose: \nimages[2]\n\nTIE.')
