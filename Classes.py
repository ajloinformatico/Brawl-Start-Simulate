import random
import functions


class Player:
    def __init__(self, name, cards_player):
        self.name = name
        self.all_cards = cards_player  # cards of the player
        self.brawler = RandomCards(functions.load_dic_from_file("brawlers"))  # all cards
        self.especial = {}
        self.super_especial = {}
        self.epico = {}
        self.mitico = {}
        self.legendario = {}
        self.load_cards()  # makes the cards deal

    def order_cards(self, cards):
        """
        Just order cards
        """
        for c, v in cards.items():
            if v == "especial":
                self.especial[c] = v
            elif v == "superespecial":
                self.super_especial[c] = v
            elif v == "epico":
                self.epico[c] = v
            elif v == "mitico":
                self.mitico[c] = v
            elif v == "legendario":
                self.legendario[c] = v

    def load_cards(self):
        """Load cards"""
        if self.all_cards == {}:
            pass  # if player dont have any card do not nothing
        else:
            self.order_cards(self.all_cards)

    def simulate(self, days: int):
        """Simulate the days"""
        dic = {}
        print("Working in your simulate")
        functions.time_sleep()
        for i in range(days):
            random_choice = self.brawler.random_card()
            dic[random_choice[0]] = random_choice[1]  # add to dic
            print(random_choice)
        self.order_cards(dic)

    def check_winner_types(self):
        """
        Check the content of the class attributes and next to the function check if
        you have gained one type or all
        """
        result = ""
        loser = True # Flag for losers jeje
        winner = 0 # Flag counter for fucking  Gods
        if functions.count(self.especial) == 3:
            result += "Congratulations you have completed  all the SPECIAL`S LETTERS!!\n"
            loser = False
            winner += 1
        if functions.count(self.super_especial) == 4:
            result += "Congratulations you have completed all the SUPER SPECIAL`S LETTERS!!\n"
            loser = False
            winner += 1
        if functions.count(self.epico) == 3:
            result += "Congratulations you have completed all the EPIC`S LETTERS!!\n"
            loser = False
            winner += 1
        if functions.count(self.mitico) == 3:
            result += "Congratulations you have completed all the Mythical MYTHICAL`S LETTERS!!\n"
            loser = False
            winner += 1
        if functions.count(self.legendario) == 3:
            result += "Congratulations you have completed all the LEGENDARY`S LETTERS!!\n"
            loser = False
            winner += 1

        return(self.check_if_the_player_has_won(result,loser,winner))


    def check_if_the_player_has_won(self, result,loser, winner):
        """
        receiving as parameters the result of the previous exercise. check if you have won if you have any row or
        if you have nothing
        """
        if not loser and winner == 5:
            return "Congratulations you have completed the game YOU HAVE ALL THE GAMES!!!"
        if not loser and winner != 5:
            return result
        return "You have not completed any type yet"


    def save_game(self):
        """
        save the game when the user leaves the game
        :return (void):
        """
        file = "players/"+ self.name.lower()
        with open(file,"w") as manf:
            for c,v in self.especial.items():
                manf.write(v+"\n")
                manf.write(c+"\n")
            for c,v in self.super_especial.items():
                manf.write(v+"\n")
                manf.write(c+"\n")
            for c,v in self.epico.items():
                manf.write(v+"\n")
                manf.write(c+"\n")
            for c,v in self.mitico.items():
                manf.write(v+"\n")
                manf.write(c+"\n")
            for c,v in self.legendario.items():
                manf.write(v+"\n")
                manf.write(c+"\n")



    def __str__(self):
        """
        Return toString of the content from the dictionaries
        :return (str): return the content of the self dics
        """
        if len(self.especial) != 0 or len(self.super_especial) != 0 or len(self.mitico) != 0 or len(self.legendario) != 0:

            result = "Brawlers:\nEspeciales = \t\t> "
            if len(self.especial) == 0:
                result += "empty"
            else:
                for c, v in self.especial.items():
                    result += c + " : " + v + "\t"

            result += "\nSuper Especiales = \t> "
            if len(self.super_especial) == 0:
                result += "empty"
            else:
                for c, v in self.super_especial.items():
                    result += c + " : " + v + "\t"

            result += "\nEpicos = \t\t\t> "
            if len(self.epico) == 0:
                result += "empty"
            else:
                for c, v in self.epico.items():
                    result += c + " : " + v + "\t"

            result += "\nMíticos = \t\t\t> "
            if len(self.mitico) == 0:
                result += "empty"
            else:
                for c, v in self.mitico.items():
                    result += c + " : " + v + "\t"

            result += "\nLegendarios = \t\t> "
            if len(self.legendario) == 0:
                result += "empty"
            else:
                for c, v in self.legendario.items():
                    result += c + " : " + v + "\t"

            return result

        else:
            result = self.name.capitalize() + " has not cards yet"
            return result


class RandomCards:
    def __init__(self, cards):
        self.cards = cards
        self.especial = {}
        self.super_especial = {}
        self.epico = {}
        self.mitico = {}
        self.legendario = {}
        self.load_cards()  # makes the cards deal

    def load_cards(self):
        """
        makes the cards deal
        :param self.cards (dic): self.cards dic of all the cards
        :return (void): just create the cards
        """
        for c, v in self.cards.items():
            if v == "especial":
                self.especial[c] = v
            elif v == "superespecial":
                self.super_especial[c] = v
            elif v == "epico":
                self.epico[c] = v
            elif v == "mitico":
                self.mitico[c] = v
            elif v == "legendario":
                self.legendario[c] = v

    def random_card(self):
        # todo apply probability
        """
        returns a random card
        :return (dic): card choice
        """
        types = ["e", "s", "ep", "m", "l"]
        type_selected = random.choice(types)
        if type_selected == "e":
            return self.random_from_dic(self.especial)
        elif type_selected == "s":
            return self.random_from_dic(self.super_especial)
        elif type_selected == "ep":
            return self.random_from_dic(self.epico)
        elif type_selected == "m":
            return self.random_from_dic(self.mitico)
        elif type_selected == "l":
            return self.random_from_dic(self.legendario)

    def random_from_dic(self, dic):
        key = random.choice(list(dic))
        for c, v in dic.items():
            if c == key:
                return c, v

    def __str__(self):
        """
        Return toString of the content from the dictionaries
        :return (str): return the content of the self dics
        """
        result = "Brawlers:\nEspeciales = \t\t> "
        for c, v in self.especial.items():
            result += c + " : " + v + "\t"
        result += "\nSuper Especiales = \t> "
        for c, v in self.super_especial.items():
            result += c + " : " + v + "\t"
        result += "\nEpicos = \t\t\t> "
        for c, v in self.epico.items():
            result += c + " : " + v + "\t"
        result += "\nMíticos = \t\t\t> "
        for c, v in self.mitico.items():
            result += c + " : " + v + "\t"
        result += "\nLegendarios = \t\t> "
        for c, v in self.legendario.items():
            result += c + " : " + v + "\t"
        return result
