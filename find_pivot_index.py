# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         i = 0
#         j = len(nums) - 1
#         left_sum = nums[i]
#         right_sum = nums[j]
#         i += 1
#         j -= 1
#         while i != j:
#             if left_sum < right_sum:
#                 left_sum += nums[i]
#                 i += 1
#             elif right_sum < left_sum:
#                 right_sum += nums[j]
#                 j -= 1
#             else:
#                 i += 1
#                 j -= 1
#         print("sums - rs: ", right_sum, "ls: ", left_sum)
#         print("indexes: ", i, j)
#         return j

# chat gbt said my solution doesn't work but it doesn't really make sense why
# actually i do know why lol, for the edge case of [-1,-1,-1,-1,0], then the left bound would
# keep moving right and converge on the right bound (0). So I got scammed :C
# heres the correct solution

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]

        return -1
