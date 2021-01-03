# Project for day 7
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ['hello','world','python']

chosen_word = random.choice(word_list)

display = ['_' for letter in chosen_word]

print ("Welcome to python Hangman \n\n")
""" print(f'Chosen word: {chosen_word}') """
print(f"{' '.join(display)}")
   

word_length = len(chosen_word)

lives = 6

completedGame = False



while not completedGame:
    guess = str(input('Type any letter: ')).lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"{' '.join(display)}")

    if guess not in chosen_word:
        lives-=1
        print(stages[lives])    
   
        if lives ==0:
            completedGame = True
            print ('You lose.')
            print(f"The chosen word was: {chosen_word}")
    