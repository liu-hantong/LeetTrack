class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res = int(dividend/divisor) 
        return res - 1 if res == 2147483648 else res