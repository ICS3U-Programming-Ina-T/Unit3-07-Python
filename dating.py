#!/usr/bin/env python3

# Created by: Ina Tolo
# Created on: Dec. 15, 2021
# This program uses compound boolean expressions
# to determine if a pair of grandparents will
# allow the user to date their grandchild.


# defines yes and no variables
yes = "yes"
no = "no"


# displays opening message
print("Today we will determine if you can date our grandchild!\n")

# gets input from the user
user_rich = input("Are you rich? (yes/no): ")
user_looks = input("Are you really good looking? (yes/no): ")
print("")

# this function checks if the user 
# can date the grandchild
# it also checks if there are any errors
def main():

    if user_rich == yes or user_looks == yes:
        print("You can date our grand child!")
    elif user_rich == yes and user_looks == no:
        print("You can date our grand child!")
    elif user_rich == no and user_looks == yes:
        print("You can date our grand child!")
    elif user_rich != yes and user_rich != no:
        print("This is invalid. Please enter a valid response.")
    elif user_looks != yes and user_looks != no:
        print("This is invalid. Please enter a valid response.")
    else:
        print("You cannot date our grandchild.")


if __name__ == "__main__":
    main()
