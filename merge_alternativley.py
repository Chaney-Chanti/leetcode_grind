# Question - Can the two strings be of different length?

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        word1_len = len(word1)
        word2_len = len(word2)
        longer_word = word1_len if word1_len > word2_len else word2_len
        iterator = 0
        while(iterator < longer_word):
            if iterator < word1_len:
                answer += word1[iterator]
            if iterator < word2_len:
                answer += word2[iterator]
            iterator += 1
        return answer

# Analysis

#Performance
#-----------

#| Metric   | Value                         |
#|----------|-------------------------------|
#| Runtime  | **37 ms** (beats **58.90%**)  |
#| Memory   | **17.18 MB** (beats **95.41%**) |

#Complexity
# Time: O(n + m) — iterate through both input strings once (n = len(word1), m = len(word2))
# Space: O(n + m) — output string of length n + m

