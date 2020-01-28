# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 19:56:08 2020

@author: iles_
"""

class Printable:
    def __repr__(self): 
        return str(self.__dict__)