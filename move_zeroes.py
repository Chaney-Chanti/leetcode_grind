# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         i = 0
#         while i < len(nums)-1:
#             print("i: ", i, "len: ", len(nums))
#             if nums[i] == 0 and nums[i+1] != 0:
#                 print("before: ", nums)
#                 nums[i] = nums[i+1]
#                 nums[i+1] = 0
#                 print("after: ", nums)
#             elif nums[i] == 0 and nums[i+1] == 0 and i != len(nums)-2:
#                 # delete current and append to end
#                 print("before: ", nums)
#                 print("deleting 0 and appending to end")
#                 del nums[i]
#                 nums.append(0)
#                 print("after: ", nums)
#                 i -= 1
#             i += 1
#         return
        

# correct solution i gacve up here....
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0  # next position for non-zero
        
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1
        
        # Fill remaining positions with zeros
        for i in range(write, len(nums)):
            nums[i] = 0
