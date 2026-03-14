class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack(s):
            if len(s) == n:
                res.append("".join(s))
                return
            if len(res) >= k:
                return

            for c in "abc":
                if not s or s[-1] != c:
                    s.append(c)
                    backtrack(s)
                    s.pop()

        backtrack([])
        return res[k-1] if len(res) >= k else ""
