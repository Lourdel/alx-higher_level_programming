#!/usr/bin/python3
def element_at(my_list, idx):
    for element in my_list:
        if idx < 0 and idx > len(my_list) - 1:
            return (None)
        else:
            element = my_list[idx]
            return (element)
