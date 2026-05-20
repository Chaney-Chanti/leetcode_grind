# Brute force solution:
# def subsetsWithDup(nums):
#     nums.sort()
#     result = set()
#     result.add(())  # Start with empty subset

#     for num in nums:                        # Outer loop: each number
#         new_subsets = set()
#         for subset in result:               # Inner loop: each existing subset
#             new_subsets.add(subset + (num,))  # Add num to every existing subset
#         result |= new_subsets               # Merge new subsets in

#     return [list(s) for s in result]

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start, current):
            result.append(current[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                current.append(nums[i])
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return result
