import unittest
from collections import Counter

def perm(s1,s2):
    if len(s1)!= len(s2):
        return False
    return sorted(s1)==sorted(s2)
  
  
def check_permutation_pythonic(str1, str2):
    if len(str1) != len(str2):
        return False
    return Counter(str1) == Counter(str2)
  
