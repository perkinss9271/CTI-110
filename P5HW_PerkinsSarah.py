#Math quiz game
#December 7, 2023
#CTI-110 P5HW Math Quiz 
#Sarah Perkins 
#

import random

print('Welcome to Math Quiz')
print()
print()

def print_menu():
    print('MAIN MENU')
    print('--------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    
print_menu()
print()

choice = int(input('Please choose one of the menu options:\n'))

num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)def main():
    display_intro()
    print_menu()
    
    option = get_user_choice()
    count = 0
    while option != 3:
        option = get_user_choice()
        
    print('Thank you for playing...')
    print('Bye!!')

def check_answer(num1, num2):
    if choice == 1:
        answer = num1 + num2
    elif choice == 2:
        answer = num1 - num2
    
    return answer

if choice == 1:
    print('  ', num1)
    print('+ ', num2)
    print()
    num_guesses = 0
    guess = int(input('Enter answer.\n'))
    num_guesses =+ 1
    
    if guess < check_answer(num1, num2):
        print('Sorry, guess is too low.')
        guess = int(input('Try again:'))
        
    if guess > check_answer(num1, num2):
        print('Sorry, guess is too high.')
        guess = int(input('Try again:'))
    
    if guess == check_answer(num1, num2):
        print('Congratulations!!!! Your answer is correct.')
        print('Number of guesses: ', num_guesses)
        print_menu()
        choice = int(input('Please choose one of the menu options:\n'))

if choice == 2:
    print('  ', num1)
    print('- ', num2)
    print()
    num_guesses = 0
    guess = int(input('Enter answer.\n'))
    num_guesses =+ 1
    
    if guess < check_answer(num1, num2):
        print('Sorry, guess is too low.')
        guess = int(input('Try again:'))
        
    if guess > check_answer(num1, num2):
        print('Sorry, guess is too high.')
        guess = int(input('Try again:'))
    
    if guess == check_answer(num1, num2):
        print('Congratulations!!!! Your answer is correct.')
        print('Number of guesses: ', num_guesses)
        print_menu()
        choice = int(input('Please choose one of the menu options:\n'))

if choice == 3:
    print('Thank you for playing...')
    print('Bye!!')
    