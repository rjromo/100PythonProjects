# Project for day 7
import random

word_list = ['hello','world','python']

chosen_word = random.choice(word_list)

display = ['_' for letter in chosen_word]


print(f'Chosen word: {chosen_word}')
print(display)
   

word_length = len(chosen_word)

while True:
    guess = str(input('Type any letter: ')).lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(display)

    """  else:
            print('Wrong')    
    """