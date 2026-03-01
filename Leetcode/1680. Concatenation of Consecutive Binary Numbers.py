class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0
        for current_num in range(1, n + 1):
            num_bits = current_num.bit_length()
            result = ((result << num_bits) | current_num) % MOD
          
        return result
