#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = (0, None) if len(sentence) == 0 else (len(sentence), sentence[:1])
    return my_tuple
