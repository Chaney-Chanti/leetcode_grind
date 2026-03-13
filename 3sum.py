# Apprently, this is just an extension of two sum and two sum II
# It's the weird skipping values to avoid duplicates that is weird/annoying to deal with
# I don't think I would be able to do this problem again ngl...


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort() # This is O(n log n ) 
        for i, v in enumerate(nums):
            if i > 0 and v == nums[i-1]: # means its the same value as before
                continue

            # Now implement two sum
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = v + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    res.append([v, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return res    
        
