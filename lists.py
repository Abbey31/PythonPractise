# # # # users = ['Dave','John','Sarah']
# # # # data = ['Dave',42,True]
# # # # emptylist = []
# # # # print("dave" in emptylist)
# # # # print(users[0])
# # # # print(users[-2])

# # # # print(users.index('Sarah'))
# # # def multiple_items(*args):
# # #     print(args)
# # #     print(type(args))

# # # multiple_items("dave",'John','sara')
# # def multi_named_items(**kwargs):
# #     print(kwargs)
# #     print(type(kwargs))
# # multi_named_items(first =)
# # CLOSURE
# #Closure is a function having access to the scope of its parent function
# # after the parent function has returned

# # def parent_function(person, coins):
# #     coins = 3

# #     def play_game():
# #         nonlocal coins
# #         coins -= 1

# #         if coins > 1:
# #             print("\n " + person + " has " +  str(coins) + "coins left.")
# #         elif coins == 1:
# #             print("\n " + person + " has " + str(coins) + "coin left.")
# #         else:
# #            print("\n" + person +  " is out of coins.")
# #     return play_game

# # tommy = parent_function("Tommy", 3)
# # jenny = parent_function("Jenny", 5)

# # tommy()
# # tommy()


# # jenny()
# # tommy()
# # F STRINGS
# person = "Dave"
# coins = 3

# print("\n" + person + " has" + str(coins) + " coins left.")
# message = "\n%s has %s coins left." %(person,coins)
# print(message)


# message = "\n{1} has {0} coins left." .format(person,coins)

# print(message)

# player = {'person':'Dave','coins': 3}

# message = "\n{person} has {coins} coins left." .format(**player)
# message = "\n{person.lower()} has {coins} coins left." .format(**player)
# print(message)

# message = f"\n{person} has {2*10} coins left."
# print(message)

# # passing formatting options
# num = 10
# print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")
# for num in range(1,11):
#     print(f"2.25 times {num} is {2.25 * num:.2f}")
# for num in range(1,11):
#     print(f"{num} divided by 4.52 is {num/4.52:.2f}")
# MODULES
# from math import pi
# import sys
# import random as me
# from enum import Enum
# import kansas
# from rocking7 import rock_paper_scissors
 
# print(pi)

# for item in dir(me):
#     print(item)

# print(kansas.capital)
# #kansas.randomfunfact()

# print(__name__)
# print(kansas.__name__)

# rock_paper_scissors()
# COMMAND LINE ARGUMENTS

def hello(name,lang):
    greetings = {
        "English":"hello",
        "Spanish":"Hola",
        "German":"Hallo",
    }
    msg = f"{greetings[lang]} {name}"
    print(msg)
if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )
    parser.add_argument(
        "-l","--lang", metavar="language",
        required=True, choices=["English","spanish","German"],
        help="The language of the greeting ."
    )

        

    


    args = parser.parse_args()
    msg = f"Hello {args.name}!"
    print(msg)


    