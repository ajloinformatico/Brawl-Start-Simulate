import os
import time


def show_players():
    """
    Shows a list of players players have a directory
    each player has their directory
    :return (str): a string with all the players
    """
    players = str()
    for p in os.scandir("./players"):
        p = str(p)[11:-2] # name of file is from 10 to -2
        if p != "info.txt": # skip info file
            players += p + "\n"
        else:
            continue
    return players


def check_exists_players():
    """
    Ensures if players exist
    :return (bool): True if exists, False if not exists
    """
    players = show_players()
    if players != "":
        return True
    return False


def check_only_one_player_exists(player: str):
    """
    Ensures if an execle player exists
    :param player (str): String of player to look for
    :return (bool): True if player exists, False if not exists
    """
    players = show_players().split()
    for p in players:
        if p == player:
            return True
    return False


def not_number(n):
    """todo show why when i write more than one letter it fails
    Check if param is a number or not
    :param n: param to check if it is a number or not
    :return (bool): True if param is a number, False if param is not a number
    """
    try:
        for i in n:
            int(i)
        return False
    except ValueError:
        return True


def create_new_user(ruta: str):
    """
    Create a new file for a new player
    :param ruta (str): name of the player
    :return (void): just create a file for player
    """
    file = open(ruta, "w")
    print("create")
    file.close()


def count_number_of_lines(ruta: str):
    """
    Count the lines of a file
    :param ruta (str): route of the file to read
    :return lines (int): an integer of all the line of the file
    """
    file = open(ruta, 'r')
    lines = (len(file.readlines()))
    file.close()
    return lines


def load_dic_from_file(ruta: str):
    """
    Load a dic from a file. This dic will contain keys as names of characters
    and values of type of characters
    :param name (str): name of the file to load
    :return (dic): return the elements of the file on a dic
    """
    dic = {}

    with open(ruta, "r") as manf:
        c = count_number_of_lines(ruta) / 2  # we need the number of lines / 2
        while (c != 0):
            c -= 1  # for each couple rest one to the counter
            value = manf.readline().rstrip()
            key = manf.readline().rstrip()
            dic[key] = value
    return dic


def time_sleep():
    """
    print sleep time
    :return (void):
    """
    for i in range(3):
        print(".", end=" ")
        time.sleep(2)
    print()


def delete_game(name:str):
    """
    Remove current file. Which is the file where there is the player
    :param name (str): player name to remove
    :return (void): just close the game after show message with sleep time
    """
    print("Removing your file")
    time_sleep()
    os.remove("players/"+name)
    print("Current player was removed\nGood bye")
    exit(0)

def count(dic):
    """
    Count the elements of a dictionaries
    :param dic (dict): standard dictionary
    :return count (int): number of elements of a dictionary
    """
    counter = 0
    for ele in dic:
        counter += 1
    return counter