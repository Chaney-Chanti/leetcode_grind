# I wasn't able to get this and needed to look at solution
# I was way overthinking the solution but am also not sure why this works
# In the ex) [2, 4, 0, 7]
# iter 1: small = 2, medium = inf
# iter 2: small = 2 , medium = inf
# iter 3: small = 0, medium = inf
# iter 4: small = 0, medium = 7 return True
# But the problem states that i < j < k and nums[i] < nums[j] < nums[k].
# In this example, the i j and k should be 0, 1, 3 represeting 2, 4, 7
# I just don't see how I could have come up with this solution.
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small = medium = float('inf')
        for num in nums:
            if num <= small:
                small = num
            elif num <= medium:
                medium = num
            else:
                return True
        return False
