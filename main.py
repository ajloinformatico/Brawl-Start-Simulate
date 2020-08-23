import os
import functions
import time
#todo add condition for info file in check functions for users
from Classes import *


def check_and_create_new(name: str):
    """
    Simple function that check to create a new player
    : param name (str): string for the new plaer
    : returns True (bool): if player was created
    : returns reply (str): if player isnt created
    """
    if functions.not_number(name) and len(name) > 1:
        print("Creating a new game for", name.capitalize()), "\n..."
        functions.time_sleep()
        return True
    else:
        return "Sorry your name is not valid."


if __name__ == "__main__":
    print("""
**************************************************
Welcome to the opening of Brawlers Stars packages"
|                |      |      |                 |
|                 |     |     |                  |
|                  |    |    |                   |
|                   | | | | |                    |
**************************************************
""")

    # Login
    while True:
        # check if exists players
        # if players exists do it
        if functions.check_exists_players():
            print(
                "Please choose a name from the list or create a new game writing a diferent name.\nIf you want to exit please"
                "enter \"end\" or \"exit\"")
            name = input("\n>>> ").lower()
            # exit
            if name == "exit" or name == "end":
                exit(0)
            # login with an user
            elif functions.check_only_one_player_exists(name):
                print("loading your game")
                functions.time_sleep()
                print("Welcome to your game ", name.capitalize())
                break

            else:
                # check if its a name
                if check_and_create_new(name):
                    # create a new user
                    functions.create_new_user("players/" + name)
                    print("s")
                    break
                else:
                    print(check_and_create_new(name))


        else:
            print(
                "Welcome to Brawl-Start-Simulate\nThere isnt any Game please create one by \"writing a name\".\nif you want to exit.\nPlease enter \"exit\" or \"end\"")

            name = input("\n>>> ").lower()
            if name == "exit" or name == "end":
                exit(0)
            if check_and_create_new(name):
                functions.create_new_user("players/" + name)

    # after login
    comands = """
    **************************************************
    > end =             exit and save
    > exit =            exit and save
    > commands =        Show commands
    > delete game =     delete the game of the current 
                        player
    > show brawlers =   shows the brawlers letters
    > my cards =        show your cards
    > simulate "days" = begin simulate of the game The 
                        simulation of the game begins 
                        according to the days 
                        entered
    **************************************************
        """
    brawlers_cards = functions.load_dic_from_file("brawlers")
    cards_player = functions.load_dic_from_file("players/" + name)
    brawlers = RandomCards(brawlers_cards)
    player = Player(name, cards_player)

    print("Enter a command from the list:\n" + comands)
    while True:
        elec = input(">>> ").lower()

        if elec == "exit" or elec == "end":
            print("Good bye " + name.capitalize() + " See you latter")
            exit(0)
        if elec == "commands" or elec == "command":
            print(comands)

        if len(elec.split()) == 2:

            if elec.split()[0] == "delete" and elec.split()[1] == "game":
                functions.delete_game(name)
            if elec.split()[0] == "show" and elec.split()[1] == "brawlers":
                print(brawlers)
            if elec.split()[0] == "my" and elec.split()[1] == "cards" or elec.split()[1] == "card":
                print(player)
            if elec.split()[0] == "simulate" and not functions.not_number(elec.split()[1]):
                days = int(elec.split()[1])
                if 0 < days <= 10:
                    player.simulate(days)
                else:
                    print("the days must be a number between 1 and 10")
            else:
                print("Sorry the command is invalid. Input \"command\" or \"commands\" to see the commands")
        else:
            print("Sorry the command is invalid. Input \"command\" or \"commands\" to see the commands")
