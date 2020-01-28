# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:33:18 2020

@author: iles_
"""
import hashlib as hl
import json

def hash_string_256(string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    """ Hashes a block and returns a unique string representation 
    
        Arguments:
            :block: The block to be hashed. 
    """
    hashable_block = block.__dict__.copy()
    hashable_block['transactions'] = [tx.to_ordered_dict() for tx in hashable_block['transactions']]
    return hl.sha256(json.dumps(hashable_block, sort_keys=True).encode()).hexdigest()