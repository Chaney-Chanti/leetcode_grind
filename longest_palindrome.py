# Did a mock style interview with claude for this one.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # Check for odd-length palindromes (center is a single character)
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            odd_palindrome = s[left + 1:right]
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            
            # Check for even-length palindromes (center is between two characters)
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            even_palindrome = s[left + 1:right]
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome
