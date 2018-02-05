#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__ = 'xu dao bin'

import sys

def test():
  args = sys.argv
  if len(args) == 1:
    print('hello, wold %s' %args[0])
  elif len(args) == 2:
    print('hello, %s' %args[1])
  else:
    print('too many arguments!')
  
if __name__ == '__main__':
  test()