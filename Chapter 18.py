import random
import sys
from Card import *

class Time(object):
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __lt__(self, other):
        return(self.hour, self.minute, self.second) < (other.hour, other.minute, other.second)
    def __gt__(self, other):
        return(self.hour, self.minute, self.second) > (other.hour, other.minute, other.second)
    def __eq__(self, other):
        return(self.hour, self.minute, self.second) == (other.hour, other.minute, other.second)

a = Time(hour=5, minute=20, second=20)
b = Time(hour=5, minute=20, second=34)

class Card(object):
    """Represents a standard playing card"""
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
    
    suit_name = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_name= [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_name[self.rank], Card.suit_name[self.suit])
    def __lt__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)
    def __gt__(self, other):
        return (self.rank, self.suit) > (other.rank, other.suit)
    def __eq__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)
        
card1 = Card(3,11)
card2 = Card(2,15)

class Deck(object):
    def __init__(self):
        self.cards =[]
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def __len__(self):
        return len(self.cards)
    def add_card(self, card):
        self.cards.append(card)
    def pop_card(self):
        return self.cards.pop()
    def shuffle(self):
        return random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
        return "deck has been sorted."
    def move_cards(self, hand, num):
        """Moves the given number of cards from the deck into the Hand.

        hand: destination Hand object
        num: integer number of cards to move
        """
        for i in range(num):
            hand.add_card(self.pop_card())

    def deal_hand(self, num_of_hands, num_of_cards_each_hand):
        if (num_of_hands * num_of_cards_each_hand) > len(self):
            hand_and_card = '\n{} hands with {} cards each is {} cards\
            \nTotal cards left in deck: {}'.format(num_of_hands, num_of_cards_each_hand, num_of_hands * num_of_cards_each_hand, len(self))
            return hand_and_card
        else:
            hands = []
            for h in range(num_of_hands):
                hand = Hand()
                for c in range(num_of_cards_each_hand):
                    hand.cards.append(self.cards.pop())
                hands.append(hand)
            return hands

deck = Deck()

class Hand(Deck):
    """Represents a hand of playing cards"""
    def __init__(self, label=''):
        self.cards = []
        self.label = label
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop.card())
    
hand = Hand('new hand')
card = deck.pop_card()
hand.add_card(card)

def main():

    # print(hand.deal_hand(2, 7))
    # print(hand)
    # # print(deck)
    # print(hand.cards)
    # deck = Deck()
    # deck.shuffle()
    # deck
    # deck.sort()
    # print(deck)
    # card1 = Card(2,11)
    # print(card1)
    # print(card1 < card2)
    # print(a > b)
    # print(deck)
    pass

if __name__ == '__main__':
    main()