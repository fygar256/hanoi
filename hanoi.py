#!/usr/bin/python3
import sys

def hanoi(n,from_,to,work):
  if (n>0):
    hanoi(n-1,from_,work,to)
    print("move #%d disk from %s to %s" % (n,from_,to))
    hanoi(n-1,work,to,from_)

hanoi(int(sys.argv[1]),'Left','Center','Right')

