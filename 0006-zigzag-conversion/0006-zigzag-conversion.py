class Solution:
    def convert(self, s: str, n: int) -> str:
        if n == 1:
            return s
        rs = [[] for i in range(n)]
        r = 0
        d = 1
        for ch in s:
            rs[r].append(ch)
            r += d
            if d == 1 and r == n - 1:
                d = -d
            if d == -1 and r == 0:
                d = -d
        ans = []
        for r in rs:
            ans.extend(r)
        return ''.join(ans)
            