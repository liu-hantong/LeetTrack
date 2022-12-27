class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lcm = math.lcm(a, b)
        left = min(a, b)
        right = lcm * n
        mod = 10 ** 9 + 7

        def check(x):
            return x // a + x // b - x // lcm
        
        while left <= right:
            mid = (left + right) // 2
            if check(mid) == n:
                if mid % a == 0 or mid % b == 0:
                    return mid % mod
                else:
                    right = mid - 1
            elif check(mid) > n:
                right = mid - 1
            else:
                left = mid + 1
