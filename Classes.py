class Player:
    def __init__(self, name, cards_you_have, cards_you_not_have):
        self.name = name
        if cards_you_have == []:
            self.cards_you_have = []
        else:
            self.cards_you_have = cards_you_have
        # not available cards list
        if cards_you_not_have == []:
            self.cards_you_not_have = []
        else:
            self.cards_you_not_have = cards_you_have




    def __str__(self):
        cards = str()
        for card in self.available_cards:
            cards += card + " "
        print(self.name + " :\n" + cards)
