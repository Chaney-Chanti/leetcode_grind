class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # stack = [asteroids[0]]
        # for i in range(1, len(asteroids)):
        #     if abs(asteroids[i]) > stack[-1] and asteroids[i] * stack[-1] < 0:
                    # problem is that I need to keep doing this if the current asteroid defeats the previous x amount of smaller asteroids
                    # going to see if making a while loop is easier 
        #         stack.pop()
        #     else:
        #         stack.append(asteroids[i])

        # =======================================================================================================================

        # stack = []
        # i = 0
        # while i < len(asteroids):
        #     # if there is opposite signs, an element is either getting popped, or the current evaluated element is skipped, or both.
        #     if not stack:
        #         stack.append(asteroids[i])
        #         i += 1
        #     if asteroids[i] * stack[-1] < 0:
        #         if abs(asteroids[i]) > stack[-1]:
        #             stack.pop()
        #         elif abs(asteroids[i]) == stack[-1]:
        #             stack.pop()
        #             i += 1
        #         else:
        #             i += 1
        #     else:
        #         stack.append(asteroids[i])
        #         i += 1
        # return stack

        # =======================================================================================================================
        # My conditional check was incorrect. I was just checking if the values were opposite signs, but its important because
        # opposite signs could also mean that are moving away from each other. 

        stack = []
        i = 0
        while i < len(asteroids):
            # if there is opposite signs, an element is either getting popped, or the current evaluated element is skipped, or both.
            if not stack:
                stack.append(asteroids[i])
                i += 1
                continue
            if asteroids[i] < 0 and stack[-1] > 0:
                if abs(asteroids[i]) > abs(stack[-1]):
                    stack.pop()
                elif abs(asteroids[i]) == abs(stack[-1]):
                    stack.pop()
                    i += 1
                else:
                    i += 1
            else:
                stack.append(asteroids[i])
                i += 1
        return stack


        # The above solution worked, here's a cleaner more canonical way

    # class Solution:
      # def asteroidCollision(self, asteroids: List[int]) -> List[int]:
      #     stack = []
  
      #     for a in asteroids:
      #         alive = True
  
      #         while alive and stack and stack[-1] > 0 and a < 0:
      #             if abs(a) > abs(stack[-1]):
      #                 stack.pop()
      #             elif abs(a) == abs(stack[-1]):
      #                 stack.pop()
      #                 alive = False
      #             else:
      #                 alive = False
  
      #         if alive:
      #             stack.append(a)
  
      #     return stack
