# Exercise - 4 Guessing numbers. Write a program that chooses an integer between 0 and 100, inclusive.
#     The program prompts the user to enter a number continuously until the number matches the chosen number.
#     For each user input, the program tells the user whether the input is too low or too high, so the user can choose
#     the next input intelligently. After the user guess correctly, the program will print: “Bravo you guess correctly after ... times”.

import random
chosen_number = random.randint(0, 100)
i = 0
while True:
    pick_number = int(input("Please pick a number: "))
    i = i + 1
    if pick_number == chosen_number:
        print("Bravo! You guessed correctly after", i, "times. ")
        quit()
    elif pick_number < chosen_number:
        print("Too low! ")
        continue
    elif pick_number > chosen_number:
        print("Too high! ")
        continue