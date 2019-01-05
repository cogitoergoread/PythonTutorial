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

class CardGame:
    """
    The CardGame class takes care of some basic chores common to all games,
    such as creating the deck and shuffling it
    """
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidHand(Hand):
    """
    A hand for playing Old Maid requires some abilities beyond the general abilities of a Hand.
    """
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}"
                        .format(self.name, card, match))
                count += 1
        return count


class OldMaidGame(CardGame):
    """
    OldMaidGame is a subclass of CardGame with a new method called
    play that takes a list of players as a parameter.
    """
    def play(self, names):
        # Remove Queen of Clubs
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))

        # Deal the cards
        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        # Remove initial matches
        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        # Play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands

        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        """
        remove_all_matches traverses the list of hands and invokes remove_matches on each
        :return: number of matches
        :rtype: int
        """
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        """
        The method play_one_turn takes a parameter that indicates whose turn it is.
        The return value is the number of matches made during this turn
        :param i: Indicate who's turn is it
        :type i: int
        :return: number of matches
        :rtype: int
        """
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        """
        ever went all the way around the circle without finding cards, it would return None and cause an error
        elsewhere in the program. Fortunately, we can prove that that will never happen
        (as long as the end of the game is detected correctly).
        :param i: Indicate who's turn is it
        :type i: int
        :return: neighbour
        :rtype: int
        """
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def print_hands(self):
        """
        Print all the hands
        """
        for hand in self.hands:
            print(hand)

if __name__ == '__main__':
    game = OldMaidGame()
    game.play(["Allen", "Jeff", "Chris"])