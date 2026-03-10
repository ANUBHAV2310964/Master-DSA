class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        from functools import cache
        MOD = 10**9 + 7

        @cache
        def f(z, o, last):
            if z == 0:
                return int(last == 1 and o <= limit)
            if o == 0:
                return int(last == 0 and z <= limit)

            if last == 0:
                res = f(z-1, o, 0) + f(z-1, o, 1)
                if z - limit - 1 >= 0:
                    res -= f(z-limit-1, o, 1)
            else:
                res = f(z, o-1, 0) + f(z, o-1, 1)
                if o - limit - 1 >= 0:
                    res -= f(z, o-limit-1, 0)

            return res % MOD

        ans = (f(zero, one, 0) + f(zero, one, 1)) % MOD
        f.cache_clear()
        return ans
