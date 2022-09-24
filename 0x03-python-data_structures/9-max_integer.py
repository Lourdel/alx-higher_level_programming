#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    else:
        max_i = my_list[0]
        for element in my_list:
            if element > max_i:
                max_i = element
        return (max_i)
