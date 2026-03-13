class Solution:
    def serverHigherAvgLoad(self, nums: List[int]) -> List[int]:

        if len(nums):
            return []

        server_sum = 0
        for num in nums:
            server_sum += num
        avg_load = server_sum / len(nums)

        output = []
        for i, num in enumerate(nums):
            if num > (2 * avg_load):
                output.append(i)
        output.sort()
        return output
            
