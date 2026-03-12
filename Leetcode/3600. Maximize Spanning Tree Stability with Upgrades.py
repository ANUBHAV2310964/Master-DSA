class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.rank[x] > self.rank[y]:
            x, y = y, x
        self.parent[x] = y
        if self.rank[x] == self.rank[y]:
            self.rank[y] += 1
        return True


class Solution:
    def maxStability(self, n, edges, k):
        uf = UnionFind(n)
        cnt = 0
        ans = float("inf")

        for u, v, s, m in edges:
            if m and uf.union(u, v):
                cnt += 1
                ans = min(ans, s)
            elif m:
                return -1

        edges.sort(key=lambda x: -x[2])

        for u, v, s, m in edges:
            if not m and uf.union(u, v):
                cnt += 1
                if cnt == n - 1 - k:
                    ans = min(ans, s)
                elif cnt == n - 1:
                    ans = min(ans, 2 * s)

        return ans if cnt == n - 1 else -1
