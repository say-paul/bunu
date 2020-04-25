#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 16:19:29 2020

@author: jhilikkundu
"""

import sys
def add(a,b):
    return a+b



def main(argv):
    if len(argv) != 3:
        sys.exit('Incorrect number of arguments, expecting two integers')
    a = int(argv[1])
    b = int(argv[2])
    print ('Sum is {}'.format(add(a,b)))

if __name__ == '__main__':
    main(sys.argv)