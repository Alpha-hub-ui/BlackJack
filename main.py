import random


class Deck:

    deck = [0, 0, 24, 24, 24, 24, 24, 24, 24, 24, 96, 24]

    def __init__(self):
        pass


    def get_random_card(self):
        card = random.randint(1, sum(self.deck))
        for i in range(12):
            card -= self.deck[i]
            if card <= 0:
                self.delCard(i)
                return i


    def mix(self):
        self.deck = [0, 0, 24, 24, 24, 24, 24, 24, 24, 24, 96, 24]


    def getDeck(self):
        return self.deck

    def delCard(self, card:int):
        if self.deck[card] > 0:
            self.deck[card] -= 1


class Player:

    def __init__(self):
        self.hand = []

    def toTakeCard(self, deck):
        self.hand.append(deck.get_random_card())
        if 11 in self.hand and 1 not in self.hand and sum(self.hand) > 21:
            self.hand[self.hand.index(11)] = 1

    def getHand(self):
        return self.hand

    def clearHand(self):
        self.hand = []


def checkTakeCardForBot(player, deck):
    sum_hand = sum(player.getHand())
    kol_positiv_kard = 0
    arr_deck = deck.getDeck()
    for i in range(2, 11):
        if i <= 21 - sum_hand:
            kol_positiv_kard += arr_deck[i]
        else:
            break
    if sum_hand < 21:
        kol_positiv_kard += arr_deck[11]
    return kol_positiv_kard / sum(arr_deck) > 0.5


def testTable(players, deck):
    dealer = []
    dealer.append(deck.get_random_card())
    for i in range(2):
        for player in players:
            player.toTakeCard(deck)

    for player in players:
        while checkTakeCardForBot(player, deck):
            player.toTakeCard(deck)

    while sum(dealer) < 17:
        dealer.append(deck.get_random_card())


    print("                               " + str(dealer))
    pl = ""
    for player in players:
        pl += str(player.getHand())
    print(pl)


deck = Deck()
players = []
for i in range(5):
    players.append(Player())

testTable(players, deck)


print(deck.getDeck())