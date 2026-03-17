from typing import List
from sortedcontainers import SortedSet

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        rows, cols = len(grid), len(grid[0])

        dr = [[0] * (cols + 2) for _ in range(rows + 1)]
        dl = [[0] * (cols + 2) for _ in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                val = grid[i - 1][j - 1]
                dr[i][j] = dr[i - 1][j - 1] + val
                dl[i][j] = dl[i - 1][j + 1] + val

        res = SortedSet()

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                res.add(grid[i - 1][j - 1])

                max_r = min(i - 1, rows - i, j - 1, cols - j)

                for r in range(1, max_r + 1):
                    s = (
                        dr[i + r][j] - dr[i][j - r] +
                        dr[i][j + r] - dr[i - r][j] +
                        dl[i][j - r] - dl[i - r][j] +
                        dl[i + r][j] - dl[i][j + r]
                        - grid[i + r - 1][j - 1]
                        + grid[i - r - 1][j - 1]
                    )

                    res.add(s)

                while len(res) > 3:
                    res.pop(0)

        return list(res)[::-1]
