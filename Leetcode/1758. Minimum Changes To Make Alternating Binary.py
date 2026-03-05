class Solution:
    def minOperations(self, s: str) -> int:
        count = 0

        for i, c in enumerate(s):
            if c != "01"[i % 2]:
                count += 1

        return min(count, len(s) - count)
