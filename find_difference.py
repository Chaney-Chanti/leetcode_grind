# class Solution:
#     def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
#         nums1_set = set(nums1)
#         nums2_set = set(nums2)

#         distinct_1 = []
#         for num in nums1:
#             if num not in nums2_set:
#                 if num not in distinct_1:
#                     distinct_1.append(num)
    
#         distinct_2 = []
#         for num in nums2:
#             if num not in nums1_set:
#                 if num not in distinct_2:
#                     distinct_2.append(num)

#         return [distinct_1, distinct_2]

# This is the correct solution. I shouldn't have needed to check for existence as that is inherently
# a part of sets in python.
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        return [
            list(set1 - set2),
            list(set2 - set1)
        ]
