#!/usr/bin/python
# Filename: func_param.py

def printMax(a, b):
    """


    a --
    b --
    """
    if a > b:
        print a, 'is maximum'
    else:
        print b, 'is maxium'


printMax(3,4)   # directly give literal values

x = 5
y = 7
printMax(x,y)   # give variables as arguments
