class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        pattern = "01"
        
        mismatch = sum(c != pattern[i & 1] for i, c in enumerate(s))
        ans = min(mismatch, n - mismatch)
        
        for i in range(n):
            mismatch -= s[i] != pattern[i & 1]
            mismatch += s[i] != pattern[(i + n) & 1]
            ans = min(ans, mismatch, n - mismatch)
        
        return ans
