def cyclic(A,K):
  length = len(A) 
  if(length == 0):
    return []
   old = A
   new = [0]*len(A)
   for i in range(K):
        new[0] = old[-1]
        new[1:] = old[:-1]
        old = new.copy() 
    return new
    
  def solution(A, K):
    length = len(A) 
    if(length == 0):
        return []
    K =  K % length 
    a = A[length-K:] + A[0:length-K] 
    return a
