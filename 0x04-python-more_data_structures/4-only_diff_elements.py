#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return ((set_1 - set_2) | (set_2 - set_1) if set_1 != {} or set_2 != {}
            else {})
