#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest score."""
    score = 0
    if a_dictionary:
        for k in a_dictionary:
            if a_dictionary[k] > score:
                score = a_dictionary[k]
                tmp = k
        return tmp
