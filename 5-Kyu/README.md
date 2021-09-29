Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []

Approach
iterate through the list and sort each word in the list and compare it to the given sorted word.
If they are equal they are anagrams
 APPROACH 2
 Using lambda function
 def anagrams(word, words):
    return filter(lambda x: sorted(word) == sorted(x), words)
