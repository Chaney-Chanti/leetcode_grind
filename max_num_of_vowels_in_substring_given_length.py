class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # initial number of vowels in the first k elements
        vowels = set("aeiouAEIOU")
        substring = s[:k]
        num_vowels = 0
        # print("substring: ", substring)
        for letter in substring:
            if letter in vowels:
                num_vowels += 1
        # print("initial num of vowels: ", num_vowels)
        max_num_of_vowels = num_vowels
        
        # slide the window
        window_sum = max_num_of_vowels # this is wrong
        for i in range(k, len(s)):
            # do max_num_of_vowels + the next element, - the previous element
            # s[i-k] is the previous element
            # s[i] in the next element
            # [includes:excludes]
            # print("string: ", s[(i-k+1):(i+1)])
            # print("next elem: ", s[i], "prev elem: ", s[i-k])
            if s[i] in vowels:
                window_sum += 1
            if s[i-k] in vowels:
                window_sum -= 1
            # print("max: ", max_num_of_vowels, "window: ", window_sum)
            max_num_of_vowels = max(max_num_of_vowels, window_sum)

        return max_num_of_vowels
