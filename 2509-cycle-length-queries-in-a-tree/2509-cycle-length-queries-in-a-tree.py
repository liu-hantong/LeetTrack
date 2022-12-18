class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        def bits(n):
            ans = 0
            while n:
                n >>= 1
                ans += 1
            return ans
        for x, y in queries:
            xs = bits(x) - 1
            ys = bits(y) - 1
            ans.append(1 + xs + ys)
            xs -= 1
            ys -= 1
            while xs >= 0 and ys >= 0:
                if x >> xs == y >> ys:
                    ans[-1] -= 2
                    xs -= 1
                    ys -= 1
                else:
                    break
        return ans
    
#            1
#         2     3
#      4     5     6 7
#   8     9    10     11 12 13 14 1
# 16 17 18 19 20 21 