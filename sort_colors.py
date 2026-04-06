# There were some nuances with this one that I couldn't figure out

# 1. The condition for the while loop
# 2. The not decrementing of iterator on a high swap but, not for low swap

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, iterator, high = 0, 0, len(nums) - 1

        while iterator <= high:
            if nums[iterator] == 0:
                nums[low], nums[iterator] = nums[iterator], nums[low]
                low += 1
                iterator += 1
            elif nums[iterator] == 2:
                nums[high], nums[iterator] = nums[iterator], nums[high]
                high -= 1
                # don't increment iterator — recheck the swapped value
            else:  # nums[iterator] == 1
                iterator += 1
