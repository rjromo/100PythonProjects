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


logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   
                   

word_list = ['hello','world','python']

chosen_word = random.choice(word_list)

display = ['_' for letter in chosen_word]

print (logo)
""" print("\n\n") """
print ("RJR \n\n")
print ("Your word has been selected randomly. Good luck! \n")
""" print(f'Chosen word: {chosen_word}') """
print(f"{' '.join(display)} \n")
   

word_length = len(chosen_word)

lives = 6

completedGame = False



while not completedGame:
    guess = str(input('Type any letter: ')).lower()
    
    if guess in display:
        print(f"You have already guessed letter: {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(f"\n{' '.join(display)} \n")

    if guess not in chosen_word:
        print(f"\nYour guess: {guess} is not in the word. You lose a life.")
        lives-=1
        print(stages[lives])    
   
        if lives ==0:
            completedGame = True
            print ('You lose.')
            print(f"The chosen word was: {chosen_word}")
    
    if "_" not in display:
        print("Hurray! You win!\n")
        print(f"The world was: {''.join(display)} \n\nCome back later!\n")
        completedGame = True