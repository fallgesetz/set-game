#!/usr/bin/env PYTHON
import random
import collections
import itertools

def is_same(attribute):
    return len(set(attribute)) == 1

def is_different(attribute):
    return len(set(attribute)) == len(attribute) 

def is_set(card_1, card_2, card_3):
    """
    Decideds whether the three given cards form a set. order doesn't matter
    """
    attribute_list = zip(card_1, card_2, card_3)
    for attribute in attribute_list:
        if not is_same(attribute) and not is_different(attribute):
            return False
    return True

def exists_set(board):
    # TODO: better way to search for this?
    for hand in itertools.combinations(board, 3):
        if is_set(*hand):
            return hand 
    return False 


shape = ["squiggle", "pill", "diamond"]
color = ["purple", "green", "red"]
fill = ["empty", "solid", "lined"]
number = ["one", "two", "three"]

def convert2num(card):
    """
    convert to numbers
    """
    return (shape.index(card[0]), color.index(card[1]), fill.index(card[2]), number.index(card[3]))

def convert2card(num_card):
    return (shape[num_card[0]], color[num_card[1]], fill[num_card[2]], number[num_card[3]])

def get_other(card_1, card_2):
    converted_card_1 = convert2num(card_1)
    converted_card_2 = convert2num(card_2)

    attributes = zip(converted_card_1, converted_card_2)
    other_card = []
    for attribute in attributes:
        f,s = attribute
        if f == s:
            other_card.append(f)
        else:
            other_card.append(3 - f - s)

    return convert2card(other_card)

def exists_partition(board):
    if not board:
        return []
    board_set = set(board)
    for partial_hand in itertools.combinations(board, 2):
        completion = get_other(*partial_hand)
        if completion in board_set:
            # recurse
            hand = partial_hand + (completion,)
            less_board = [x for x in board if x not in hand] 
            if not less_board:
                return hand
            partition = exists_partition(less_board)
            if partition:
                return list(partition) + [[hand]]
    return False

class SetGame(object):
    def shuffle(self):
        """
        misnamed...slightly. This just generates the deck
        """
        self.cards = []
        for i in shape:
            for j in color:
                for k in fill:
                    for l in number:
                       self.cards.append((i,j,k,l))

    def __init__(self, with_replacement = True):
        self.with_replacement = with_replacement
        self.board = []
        self.shuffle()

    def get_random_card(self):
        num = random.randint(0, len(self.cards) - 1)
        if not self.with_replacement:
            card = self.cards.pop(num)
        else:
            card = self.cards[num]
        return card 

    def wipe_board(self):
        self.board = []

    def get_board(self):
        while len(self.board) < 12 and self.cards:
            self.board.append(self.get_random_card())
        return self.board

    def remove_card(self, card):
        """docstring for remove_card"""
        self.board.pop(self.board.index(card))

    def play_set(self, card_1, card_2, card_3):
        """
        removes card_1, card_2, and card_3 from the board
        """
        self.remove_card(card_1)
        self.remove_card(card_2)
        self.remove_card(card_3)

def play():

    """docstring for play"""
    pass
