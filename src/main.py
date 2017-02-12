# coding:utf-8
from numpy import *
import time

source = ("Pen", "Pineapple", "Apple", "Pen")

def IsApplePen(array):
    if (tuple(array))[::-1]==source[2:]:
        print "    Oh! " + "-".join(array[::-1]) + "!"
        time.sleep(0.5)

def IsPinapplePen(array):
    if tuple(array)==source[:2]:
        print "    Oh! " + "-".join(array[::-1]) + "!"
        time.sleep(0.5)

def main():
    ppap = []
    while tuple(ppap)!=source:
        temp = random.choice(source)
        
        if temp=='Apple':
            print "I have an " + temp + "."
        else:
            print "I have a "  + temp + "."
        time.sleep(0.5)

        ppap.append(temp)
        if len(ppap) > 4:
            ppap.pop(0)
        if len(ppap) > 2:
            IsApplePen(ppap[-2:])
            IsPinapplePen(ppap[-2:])

    print "-".join(ppap)

main()