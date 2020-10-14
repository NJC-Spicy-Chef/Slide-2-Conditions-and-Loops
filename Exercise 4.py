# Restaurant Seating: Write a program that asks the user how many people are in their
# dinner group. If the answer is more than eight, print a message saying they’ll have to wait
# for a table. Otherwise, report that their table is ready.

group_size = input("Good evening, how many people are in your group tonight? ")
group_size = int(group_size)

if group_size > 8:

    print("I'm sorry you will have to wait for your table.")

else:
    print("Follow me please, your table is ready.")



