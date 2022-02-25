#sum of a series = n*(n+1)//2)
def solution(A):
    n = len(A)+1
    return (n*(n+1)//2) - sum(A)
  
