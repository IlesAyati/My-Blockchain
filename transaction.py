# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:48:43 2020

@author: iles_
"""
from collections import OrderedDict
from utility.printable import Printable

class Transaction(Printable):
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
    
    def to_ordered_dict(self):
        return OrderedDict([('sender', self.sender), 
                            ('recipient', self.recipient), 
                            ('amount', self.amount)])
