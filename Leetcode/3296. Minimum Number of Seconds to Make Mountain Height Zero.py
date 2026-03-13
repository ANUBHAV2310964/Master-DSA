from typing import List
from math import sqrt

class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

        def can_finish(t: int) -> bool:
            height = 0
            for w in workerTimes:
                n = int(sqrt(2 * t / w + 0.25) - 0.5)
                height += n
            return height >= mountainHeight

        left, right = 1, 10**16

        while left < right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid
            else:
                left = mid + 1

        return left
