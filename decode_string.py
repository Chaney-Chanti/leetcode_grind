# Too difficult to even start programming, had an idea, but just prompted for this one. Wanted to understand solution
# first. I think if I see a similar problem I can try again.
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                # Pop characters until we find '['
                segment = []
                while stack[-1] != '[':
                    segment.append(stack.pop())
                stack.pop()  # remove '['
                
                # Pop the number (may be multi-digit)
                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())
                
                # Repeat and push back
                k = int(''.join(reversed(num)))
                stack.extend(list(''.join(reversed(segment)) * k))
        
        return ''.join(stack)
