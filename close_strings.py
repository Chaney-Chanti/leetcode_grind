# from collections import defaultdict
# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         # initial thoughts:
#         # in other words, operation 1 is just saying if the occurrences of 
#         # each letter in both strings are identical

        
#         # operation 2 means that if everything else is the same, but if two letters
#         # have identical counts, then that works too. So maybe I can create a set to ignore the identical
#         # characters, and then if the frequencies are the same and the length of the unique letters are 
#         # the same, then we're good.

#         word1_freq = defaultdict(int)
#         word2_freq = defaultdict(int)

#         for letter in word1:
#             word1_freq[letter] += 1
#         for letter in word2:
#             word2_freq[letter] += 1

#         # return set(word1_freq.values()) == set(word2_freq.values()) and set(word1_freq.keys()) == set(word2_freq.keys())
#         # i don't really understand why the order of frequencies matters, but the order of the keys does not matter

#         return sorted(word1_freq.values()) == sorted(word2_freq.values()) and \
#                set(word1_freq.keys()) == set(word2_freq.keys())

            
# Cleaner solution
# the Counter class seems kinda op
from collections import Counter

class Solution:
    def closeStrings(self, word1, word2):
        f1, f2 = Counter(word1), Counter(word2)
        return set(f1) == set(f2) and sorted(f1.values()) == sorted(f2.values())
