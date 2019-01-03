"""
http://openbookproject.net/thinkcs/python/english3e/collections.html
"""
from functools import total_ordering
from typing import List


@total_ordering
class Card:
    """
     There are fifty-two cards in a deck, each of which belongs to one of four suits and one of thirteen ranks.
     The suits are Spades, Hearts, Diamonds, and Clubs (in descending order in bridge).
     The ranks are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, and King. Depending on the game that we are playing,
     the rank of Ace may be higher than King or lower than 2.
     The rank is sometimes called the face-value of the card.
    """
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def __repr__(self):
        return "Card(S:{}, R:{})".format(self.suit, self.rank)

    def __eq__(self, other):
        if type(other) is type(self):
            return self.__dict__ == other.__dict__
        return False

    def __lt__(self, other):
        if type(other) is type(self):
            return self.to_rannum() < other.to_rannum()
        return NotImplemented

    def to_rannum(self):
        """
        Create a numeric representtion of te card
        :return: 14 * suit + raank
        :rtype: int
        """
        return 14 * self.suit + self.rank

class Deck:
    """
    A deck is made up of cards, so each Deck object will contain a list of cards as an attribute.
    Many card games will need at least two different decks — a red deck and a blue deck.
    """
    cards: List[Card]

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * (i % 4)+ str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        """
        If a deck is perfectly shuffled, then any card is equally likely to appear anywhere in the deck,
        and any location in the deck is equally likely to contain any card.
        """
        import random
        rng = random.Random()  # Create a random generator
        rng.shuffle(self.cards)  # uUse its shuffle method

    def remove(self, card):
        """
        takes a card as a parameter, removes it, and returns True if the card was in the deck and False otherwise
        :param card:
        :type card: Card
        :return: True if the card was in the deck
        :rtype: bool
        """
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        """
         to remove and return the top card
        :return: the top card
        :rtype: Card
        """
        return self.cards.pop()

    def is_empty(self):
        """
        returns True if the deck contains no cards
        :return: True if the deck contains no cards
        :rtype: bool
        """
        return self.cards == []

    def deal(self, hands, num_cards=999):
        """
        we want to deal cards from the Deck into hands
        :param hands: hands to deal to
        :type hands: Hand
        :param num_cards: number of cards to deal
        :type num_cards: int
        """
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break  # Break if out of cards
            card = self.pop()  # Take the top card
            hand = hands[i % num_hands]  # Whose turn is next?
            hand.add(card)  # Add the card to the hand

class Hand(Deck):
    """
    represent a hand of cards
    """
    def __init__(self, name=""):
       self.cards = []
       self.name = name

    def add(self, card):
        """
         it is necessary to add cards from the deck
        :param card: a card to add
        :type card: Card
        """
        self.cards.append(card)


    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)

# 23.5. The CardGame class