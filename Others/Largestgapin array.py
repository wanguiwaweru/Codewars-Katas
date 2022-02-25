"""
Given an unsorted array of length N, and we have to find the largest gap between any two elements of the array. 
In simple words, find max(|Ai-Aj|) where 1 ≤ i ≤ N and 1 ≤ j ≤ N.
Input : arr = {3, 10, 6, 7}
Output : 7"""

def largest_gap(arr):
    return max(arr)-min(arr)

def largestGap(arr):
    mini = arr[0]
    maxi = arr[0]

    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
        if arr[i] < mini:
            mini = arr[i]
    return abs(maxi-mini)
