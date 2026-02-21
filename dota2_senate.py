# I couldn't figure this one out without basically getting a lot of hints
# It's because I neglected, setting up a separate queue, and especially a separate queue for the radiants and dires
# Then I had to figure out the moving the radiant or dire banner to the back of the queue by adding its index and the size of len
# So basically 3 things in total you needed to figure out, where I could not figure out any of them.
# 1. Store the people by their position (index)
# 2. Create 2 separate queues for the parties
# 3. After a member takes a turn, add them to the back of their respective queue + the len(senate) 


# from collections import deque
# class Solution:
#     def predictPartyVictory(self, senate: str) -> str:
#         dire_queue = deque()
#         radiant_queue = deque()

#         # setup party queues
#         for index, value in enumerate(senate):
#             if value == "R":
#                 radiant_queue.append(index)
#             else:
#                 dire_queue.append(index)

#         # process queues
#         while radiant_queue and dire_queue:
#             if dire_queue[0] < radiant_queue[0]:
#                 radiant_queue.popleft()
#                 dire_queue.append(dire_queue[0] + len(senate))
#                 dire_queue.popleft()
#             else:
#                 dire_queue.popleft()
#                 radiant_queue.append(radiant_queue[0] + len(senate))
#                 radiant_queue.popleft()
        
#         if not radiant_queue:
#             return "Dire"
#         else:
#             return "Radiant"


#===================================================================================================
# Canonical / Cleaner solution 

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)

        # Initialize queues with indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        # Simulate rounds
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()

            if r < d:
                # Radiant senator acts first
                radiant.append(r + n)
            else:
                # Dire senator acts first
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"

        
