#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary) > 0:
        return max(
            a_dictionary.keys(),
            key=(lambda new_k: a_dictionary[new_k]))
    return None