import os
import sys
import re 

def increment_star (n):
    for i in range (0, n):
        for j in range (0, i+1):
            print ("*", end=" ")
        print("\r") 

def decrement_star (n):
    n = n + 1
    #print (n)
    for i in range (n, 0, -1):
        for j in range (i-1, 0, -1):
            print ("*", end = " ")
        print ("\r")


if (__name__ == "__main__"):
    n = 10
    increment_star (n)
    decrement_star (n)
