#y is the target, d is th fixed jump x is current position
import math

def solution(X, Y, D):
   distance = Y - X
   if distance % D == 0:
      return distance//D
   else:
      return distance//D + 1

def solution(X,Y,D):
   return (Y - X) // D if (Y - X) % D == 0 else (Y - X) // D + 1

def solution(X,Y,D):
   return math.ceil((Y-X)/D)
