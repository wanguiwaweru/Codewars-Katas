#A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
import unittest
def gap(n):
    b = bin(n)[2:]
    b = b.strip("0")
    l = b.split("1")
    return len(max(l, key=len))
