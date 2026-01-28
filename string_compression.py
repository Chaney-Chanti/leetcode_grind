# This is difficult because we cannot use sets, hashes, or stacks because that violates 
# doing this problem in constant space.

# My initial thought is to assume that the array is always sorted, meaning that the a's
# will be next to each other, so the moment the next character changes, then we know that
# we are on a new letter

class Solution:
    # def compress(self, chars: List[str]) -> int:
    #     counter = 0
    #     i = 0
    #     breakpoint = 0
    #     curr_char = chars[0]
    #     while i < len(chars)-1:
    #         if chars[i+1] == chars[i]:
    #             counter += 1
    #         else:
    #             # then we know we are the end of consecutive chars
    #             # modify the input array
    #             counter += 1
    #             chars[breakpoint:i+1] = [curr_char, str(counter)]
    #             # now process the new char
    #             breakpoint += 2
    #             i = breakpoint
    #             curr_char = chars[i]
    #             counter = 0
    #         i += 1
    #     return len(chars)    

    # I gave up at this point =, heres ths correct solution
    def compress(self, chars: List[str]) -> int:
        write = 0  # Where we write compressed output
        read = 0   # Scans through the input

        while read < len(chars):
            char = chars[read]
            count = 0

            # Count the run of identical characters
            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # Write the count if > 1
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write

