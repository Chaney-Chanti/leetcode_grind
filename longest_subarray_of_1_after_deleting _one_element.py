# Honestly this and the max consecutive ones
# were difficult, had to look at the solution
# just doesn't make much sense to me how people
# got these solutions in 15 mins
# I think I can look at a question and know to use the sliding
# window approach, but the specific implementation is difficult for me
# to see.

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        i = 0
        zeros = 0
        max_len = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeros += 1
            # bring left bound in
            while zeros > 1:
                if nums[i] == 0:
                    zeros -= 1
                i += 1
            # subtract 1 because one element must be deleted
            max_len = max(max_len, j - i)
        return max_len
