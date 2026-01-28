# Hoenstly not bad given a hint
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_area = 0
        
        while i < j:
            y = height[i] if height[i] < height[j] else height[j]
            x = j - i
            area = x * y
            if area > max_area:
                max_area = area
            # Move the pointer with the smaller height
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_area
        
