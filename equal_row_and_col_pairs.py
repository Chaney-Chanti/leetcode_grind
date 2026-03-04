# Did this problem twice, but forgot the solution
# involves creating a hashmap of all the rows, then iterating through all the columns and seeing if they are in the hash.

from collections import defaultdict
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        answer = 0
        counts = defaultdict(int)
        for row in grid:
            counts[tuple(row)] += 1
        cols = list(zip(*grid))
        print(counts, cols)
        for col in cols:
            if tuple(col) in counts:
                answer += counts[tuple(col)]
        return answer

################### Canonical Solution ##############################

# from collections import Counter
# from typing import List

# class Solution:
#     def equalPairs(self, grid: List[List[int]]) -> int:
#         # Count row patterns
#         row_count = Counter(tuple(row) for row in grid)

#         # Compare with column patterns
#         ans = 0
#         for col in zip(*grid):
#             ans += row_count[col]

#         return ans
        
            
