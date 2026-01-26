class Solution:
    def reverseWords(self, s: str) -> str:
        result = [s for s in s.split(" ") if s]
        return " ".join(result[::-1])
