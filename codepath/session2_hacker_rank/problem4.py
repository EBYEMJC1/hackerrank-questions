#!/bin/python3

import math
import os
import random
import re
import sys
import ast



#
# Complete the 'get_top_player' function below.
#
# The function is expected to return a STRING.
#

def get_top_player(dictionary):
    high_score = float('-inf')
    top_player = ""
    #print(dictionary)
    for name, score in dictionary.items():
        if score > high_score:  
            high_score = score
            #print(high_score)
            top_player = name
            #print(top_player)
    return top_player