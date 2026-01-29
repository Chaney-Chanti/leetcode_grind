# # This is a time limit exceeds unfort... which is O(n*k) where n is the size of the list and k is the size of the window
# basically needed to calculate the previous sum.
# from typing import List

# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         max_avg = float('-inf')
#         for i in range(len(nums) - k + 1):  # make sure the window is in bounds
#             window = nums[i:i+k]  # slice of length k
#             avg = sum(window) / k
#             max_avg = max(max_avg, avg)
#         return max_avg

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]

        # initial sum of the first k elements
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        # slide the window
        for i in range(k, len(nums)):
            # do windows_sum + the next element, - the previous element
            window_sum += nums[i] - nums[i - k]
            # update the max sum
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
        
