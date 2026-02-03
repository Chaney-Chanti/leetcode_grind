class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_altitude = 0
        altitudes = [0]
        for num in gain:
            curr_altitude += num
            altitudes.append(curr_altitude)
        print(altitudes)
        return max(altitudes)
