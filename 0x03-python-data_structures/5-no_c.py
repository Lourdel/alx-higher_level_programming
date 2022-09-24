#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for xter in my_string:
        if xter != 'c' and xter != 'C':
            new_str += xter
    return (new_str)
