def solution(A):
    hashmap = {}
    for i in A:
        if i in hashmap:
            hashmap[i]+=1
        else:
            hashmap[i] = 1
    for k,v in hashmap.items():
        if v % 2 !=0:
            return k
