#!/usr/bin/env PYTHON
import random
import collections
import itertools

def hash_attribute(attribute):
    hash = collections.defaultdict(int) 
    for i in attribute:
        hash[attribute] += 1
    return hash.keys()

def is_same(attribute):
    return len(hash_attribute(attribute)) == 1

def is_different(attribute):
    return len(hash_attribute(attribute)) == 3

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
    # TODO: what's the non-bruteforce way of doing this
    for hand in itertools.combinations(board, 3):
        if not is_set(*hand):
            return False
    return True

def find_set(board):
    # TODO: implement
    pass

class SetGame(object):
    shape = ["squiggle", "pill", "diamond"]
    color = ["purple", "green", "red"]
    fill = ["empty", "solid", "lined"]
    number = ["one", "two", "three"]

    def shuffle():
        self.cards = []
        for i in shape:
            for j in color:
                for k in fill:
                    for l in number:
                       self.cards.append((i,j,k,l))

    def __init__(self, with_replacement = True):
        self.with_replacement = with_replacement

    def get_random_card():
        num = random.randint(0, len(self.cards))
        if not with_replacement:
            self.cards.pop(num)
        return cards[num]

    def get_board():
        # TODO: does not behave correctly
        if not board in self:
            self.board = []
        while len(self.board) < 12:
            self.board.append(self.get_random_card())
        return self.board

