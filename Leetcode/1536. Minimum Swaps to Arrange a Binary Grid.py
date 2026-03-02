class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)
        pos=[max([j for j,x in enumerate(row) if x],default=-1) for row in grid]
        ans=0
        
        for i in range(n):
            j=i
            while j<n and pos[j]>i:
                j+=1
            if j==n:
                return -1
            ans+=j-i
            pos[i:j+1]=[pos[j]]+pos[i:j]
        
        return ans
