#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:19:29 2020

@author: jhilikkundu
"""

import sys
def add(a,b):
# a=int(input("enter a number-"))
# b=int(input("enter 2nd no-"))
    return a+b



def main(argv):
    if len(argv) != 3:
        print('Enter two numeric value')
        raise Exception('Incorrect number of arguments')
    a = int(argv[1])
    b = int(argv[2])
    print (' output is {}'.format(add(a,b)))

if __name__ == '__main__':
    main(sys.argv)