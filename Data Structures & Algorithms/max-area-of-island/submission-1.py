from typing import List

class Solution:

    def dfs(self, row, col, grid) -> int:
        rows, cols = len(grid), len(grid[0])

        if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0):
            return 0

        grid[row][col] = 0  # mark visited by "sinking" the land
        
        return 1 + (
            self.dfs(row + 1, col, grid) +
            self.dfs(row - 1, col, grid) +
            self.dfs(row, col + 1, grid) +
            self.dfs(row, col - 1, grid)
        )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.dfs(row, col, grid))

        return max_area