class Solution:
    def largestSubmatrix(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        hist = [0] * n
        ans = 0

        for row in matrix:
            for i in range(n):
                hist[i] = hist[i] + 1 if row[i] else 0

            for i, h in enumerate(sorted(hist)):
                ans = max(ans, h * (n - i))

        return ans
