import random

class Player:
    #todo view to this class
    def __init__(self, name, cards_you_have, cards_you_not_have = None):
        self.name = name
        if cards_you_have == {}:
            self.cards_you_have = {}
        else:
            self.cards_you_have = cards_you_have
        # not available cards list
        if cards_you_not_have == None:
            self.cards_you_not_have = {}
        else:
            self.cards_you_not_have = cards_you_have

    def __str__(self):
        cards = str()
        result = str()
        for card in self.available_cards:
            cards += card + " "
            result = self.name + " :\n" + cards
        return result

class RandomCards:
    def __init__(self, cards):
        self.cards = cards
        self.especial = {}
        self.super_especial = {}
        self.epico = {}
        self.mitico = {}
        self.legendario = {}
        self.load_cards() # makes the cards deal



    def load_cards(self):
        """
        makes the cards deal
        :param self.cards (dic): self.cards dic of all the cards
        :return (void): just create the cards
        """
        for c,v in self.cards.items():
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
        print(type_selected)
        if type_selected == "e":
            return random.choice(self.especial)
        elif type_selected == "s":
            return random.choice(self.super_especial)
        elif type_selected == "ep":
            return random.choice(self.epico)
        elif type_selected == "m":
            return random.choice(self.mitico)
        elif type_selected == "l":
            return random.choice(self.legendario)



    def __str__(self):
        """
        Return toString of the content from the dictionaries
        :return (str): return the content of the self dics
        """
        result = "Brawlers:\nEspeciales = \t"
        for c,v in self.especial.items():
            result += c + " : " + v + "\t"
        result += "\nSuper Especiales = \t"
        for c,v in self.super_especial.items():
            result += c + " : " + v + "\t"
        result += "\nEpicos = \t"
        for c,v in self.mitico.items():
            result += c + " : " + v + "\t"
        result += "\nMíticos = \t"
        for c,v in self.mitico.items():
            result += c + " : " + v + "\t"
        result += "\nLegendarios = \t"
        for c, v in self.legendario.items():
            result += c + " : " + v + "\t"
        return  result