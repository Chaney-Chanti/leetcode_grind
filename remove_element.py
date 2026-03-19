class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     left = 0
    #     right = len(nums) - 1
    #     counter = 0
    #     if len(nums) == 1 and nums[0] == val:
    #         return 0

    #     while left < right:
    #         print("left: ", left, "right: ", right)
    #         while nums[right] == val and right > 0:
    #             right -= 1
    #             counter += 1
    #         print(" shifting right pointer to left | left: ", left, "right: ", right)
    #         if nums[left] == val: # swap
    #             counter += 1
    #             nums[left] = nums[right]
    #             nums[right] = val
    #             right -= 1
    #             print("swapping: ", nums)
    #         left += 1

    #     print("returning: ", len(nums) - counter)
    #     return len(nums) - counter



# ended up giving up and prompting claude... its so much simpler than the swapping method I thought I had
# to do based on hint 2.... I already knew my solution was wrong based on how complicated it was looking.

    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        return left
