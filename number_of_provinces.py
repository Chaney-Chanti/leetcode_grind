from collections import deque

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        queue = deque()
        visited = set()
        num_provinces = 0

        for city in range(len(isConnected)):
            if city not in visited:
                num_provinces += 1
                queue.append(city)
                visited.add(city)
                while queue:
                    current = queue.popleft()
                    for index, connection in enumerate(isConnected[current]):
                        if connection == 1 and index not in visited:
                            queue.append(index)
                            visited.add(index)

        return num_provinces
