# This problem took just under 2 hours. If I did not look at the hints I would not have gotten it
# Also the hints did not really help with the solution because .count in Python takes too long,
# was getting memory and time limit exceeds
# time limit because I was looping through k // 2, but if k = 1,000,000 and the list is [500,000, 500,000] then im looping
# through 1-499,999 uselessly. Just loop through the array
# memory limit because .get method in python dicts don't modify the data structure.
# if using a defaultdict(int) auto sets the keys to 0 when adding the keys to the dict so when i was iterating through 1-499,999.
# i was also creating a new entry in the dict everytime.

from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        op_counter = 0
        i = 0
        for num in nums:
            complement = k - num
            if counter[complement] > 0:
                op_counter += 1
                counter[complement] -= 1
            else:
                counter[num] += 1

        return op_counter
