# coding: utf-8

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # create a new block and add into chain
        pass

    def new_transaction(self):
        # add a new transaction into list
        pass

    @staticmethod
    def hash(block):
        # hash block
        pass

    @property
    def last_block(self):
        # return the last chain
        pass