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
        # todo check why it repeats
        dic = {}
        print("working in your simulate")
        functions.time_sleep()
        for i in range(days):
            random_choice = self.brawler.random_card()
            dic[random_choice[0]] = random_choice[1]  # add to dic
            print(random_choice)
        self.order_cards(dic)

    def __str__(self):
        #todo check if changes works
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
        for c, v in self.mitico.items():
            result += c + " : " + v + "\t"
        result += "\nMíticos = \t\t\t> "
        for c, v in self.mitico.items():
            result += c + " : " + v + "\t"
        result += "\nLegendarios = \t\t> "
        for c, v in self.legendario.items():
            result += c + " : " + v + "\t"
        return result
