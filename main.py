import os
import functions
from Classes import *





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
    comands ="""
**************************************************
> end = exit and save
> exit = exit and save
> delete game = delete the game of the current 
                player
> simulate "days" = begin simulate of the game The 
                    simulation of the game begins 
                    according to the days 
                    entered
**************************************************

    """

    # First Ensures if there is any player
    if functions.check_exists_players():
        while(True):
            print("Please Choose a name o create a new or create a new game writing a different name\nIf ypu want to exit write end or exit")
            print(functions.show_players())
            name = input("\n>>> ").lower() # all names will be saves on minuscule

            if name == "exit" or name == "end":
                print("Goodbye person I do not know I hope you execute me soon")
                exit()

            # If player input exists continue with this name
            elif functions.check_only_one_player_exists(name):
                print("Welcome to your game "+ name.capitalize())
                break
            else:
                if functions.not_number(name):
                    functions.create_new_user(name)
                    print("Welcome to your new game "+ name.capitalize())
                    break
                else:
                    print("Sorry you must write a no fake game ma friend")
                # but if this name not exists check if its a name an create new game


    # If there isnt any player
    else:
        while(True):
            print("There are no saved games. Please enter a name for your game. Your characters will be saved when you write end")
            name = input("\n>>> ").lower()

            if name == "fin" or name == "end":
                print("Goodbye person I do not know I hope you execute me soon")

            elif functions.not_number(name):
                print("Welcome to your new game " + name.capitalize())
                break
            else:
                print("Sorry you must write a no fake game ma friend")


    brawlers = functions.load_dic_from_file("brawlers")
    cards_player = functions.load_dic_from_file("players/"+name)
    # player = Player(name,functions.load_game(name), )



