# class RecentCounter:

#     def __init__(self):
#         self.requests = []

#     def ping(self, t: int) -> int:
#         counter = 0
#         self.requests.append(t)
#         for request in self.requests:
#             if request in range(t - 3000, t + 1):
#                 counter += 1

#         # popping is a slow operation, try and avoid when you can
#         i = 0
#         while i < len(self.requests) - counter:
#             self.requests.pop(0)
#             i += 1

#         return counter

# Canonical solution
from collections import deque

class RecentCounter:
    def __init__(self):
        self.q = deque()

    def ping(self, t: int) -> int:
        self.q.append(t)

        while self.q[0] < t - 3000:
            self.q.popleft()

        return len(self.q)
    
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
