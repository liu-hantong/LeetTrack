class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        return n - self.countSpecialNumbers(n)
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        
        @cache
        def f(i, mask, isLimit, isNum):
            if i == len(s):
                return int(isNum)
            res = 0
            if not isNum:
                res = f(i + 1, mask, False, False)
            up = int(s[i]) if isLimit else 9
            for num in range(1 - int(isNum), up + 1):
                if (mask >> num) & 1 == 1:
                    continue
                res += f(i + 1, mask | (1 << num), isLimit and num == up, True)
            return res
        
        return f(0, 0, True, False)
