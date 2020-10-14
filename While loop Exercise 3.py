# Exercise - 3 Modify exercise 2 to prompt the user to provide a number, then determine that the number is even or odd.
# The program needs to ask the user if she wants to continue or not. If yes, then the program asks for another number,
# if No, then the program ends.

while True:
    # Get a number from the user.
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("The number", number, "is an even number. ")

    else:
        print("The number", number, "is an odd number. ")

    answer = input("Would you like to continue? [Yes / No?] ")

    if answer.lower() == "yes":
        continue
    else:
        quit()