class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * 26
        for i in range(0, n):
            index = ord(s[i]) - ord('a')
            left = max(0, index - k)
            right = min(25, index + k)
            dp[index] = max([dp[j] for j in range(left, right + 1)]) + 1
        return max(dp)