from typing import List
from collections import deque

class Solution:

    def dfs(self, r, c, grid, visited) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque([(r, c)])
        visited.add((r, c))
        area_counter = 1

        while queue:
            # if we do pop instead of popleft we get a dfs, it becomes lifo instead of fifo
            row, col = queue.pop()

            # we still want the row offset because we still need to be able to look around
            for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + row_offset, col + col_offset

                if (0 <= new_row < len(grid) and
                    0 <= new_col < len(grid[0]) and
                    grid[new_row][new_col] == 1 and
                    (new_row, new_col) not in visited):
                    area_counter += 1
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))

        return area_counter

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # we still need to be able to iterate
        rows, cols = len(grid), len(grid[0])
        # we still need to know where we've been
        visited = set()
        area_counter = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = self.dfs(row, col, grid, visited)
                    # this is doing a replace, if the thing we see newly is larger it gets replaced
                    area_counter = max(area_counter, max_area)

        return area_counter