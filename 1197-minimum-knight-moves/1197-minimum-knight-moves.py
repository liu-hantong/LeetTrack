class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        direcs = [(2, 1), (-2, -1), (-2, 1), (2, -1), (1, 2), (-1, -2), (-1, 2), (1, -2)]
        queue = deque([(0, 0, 0)])
        visited = set()
        visited.add((0, 0))
        while queue:
            i, j, step = queue.pop()
            if i == x and j == y:
                return step
            for m, n in direcs:
                _i = i + m
                _j = j + n
                if (_i, _j) not in visited:
                    visited.add((_i, _j))
                    queue.appendleft((_i, _j, step + 1))