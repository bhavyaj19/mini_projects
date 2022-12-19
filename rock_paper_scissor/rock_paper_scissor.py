from optparse import Values
import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_pick = input("Type ROCK/PAPER/SCISSORS or Q to quit: ").lower()
    if user_pick == 'q':
        break

    if user_pick not in options:
        print("Enter correct value!")
        continue

    random_number = random.randint(0, 2)
    comp_pick = options[random_number]

    print('Computer picked',comp_pick)

    if user_pick == 'rock' and comp_pick == 'scissors':
        print('You won :)')
        user_wins += 1

    elif user_pick == 'paper' and comp_pick == 'rock':
        print('You won :)')
        user_wins += 1

    elif user_pick == 'scissors' and comp_pick == 'paper':
        print('You won :)')
        user_wins += 1

    else:
        computer_wins += 1
        print('You lose :(')

print('You won ', user_wins, ' times')
print('Computer won ', computer_wins, ' times')

print("Goodbye!")
