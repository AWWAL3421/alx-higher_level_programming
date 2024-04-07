#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None:
        my_list = []
    
    new_list = [number % 2 == 0 for number in my_list]
    return new_list
