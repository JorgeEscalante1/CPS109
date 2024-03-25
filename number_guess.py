"""Guess a number between 1 and 10"""

import random
guess = int(input('Guess a number between 1 and 10: '))
number = random.randrange(1, 11)
count = 1

while guess != number:
    count += 1
    guess = int(input(f'Nope! guessed {guess}. Please guess again: '))
print(f'Yes! THe number chosen is {number} in {count} tries.')