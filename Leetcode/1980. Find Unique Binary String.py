class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        mask = 0
        
        for s in nums:
            mask |= 1 << s.count("1")
        
        n = len(nums)
        
        for i in range(n + 1):
            if not (mask >> i) & 1:
                return "1" * i + "0" * (n - i)
