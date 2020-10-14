# Ask the user for a number, and then report whether the number is a multiple of 10 or not. '''
# Exercise - 1 Modify this assignment in order to do it in a loop.  The loop should end once the user presses “q” or “Q”.'''

while True:
    try:
        multiple_ten = input("Please input a number or press 'Q' to quit: ")

        if multiple_ten.upper() == "Q":
            break

        elif int(multiple_ten) % 10 == 0:
            print(str(multiple_ten), "is a multiple of 10. ")

        else:
            print(multiple_ten, "is not a multiple of 10. ")
            continue

    except ValueError:
        print("That is not a valid input.")
        continue

