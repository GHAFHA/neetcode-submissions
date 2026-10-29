from typing import List
from collections import deque

class Solution:
    def bfs(self, queue: deque, grid: List[List[int]], fresh_fruit_count: int) -> int:
        minute = 0
        rows, cols = len(grid), len(grid[0])

        while queue and fresh_fruit_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        fresh_fruit_count -= 1
                        queue.append((nr, nc))

            minute += 1

        return minute if fresh_fruit_count == 0 else -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_fruit_count = 0
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_fruit_count += 1
                elif grid[r][c] == 2:
                    queue.append((r, c))

        return self.bfs(queue, grid, fresh_fruit_count)