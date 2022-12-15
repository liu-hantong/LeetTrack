class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0 for i in range(5)] for j in range(n + 1)]
        dp[0][0] = 0          # buy nothing
        dp[0][1] = -prices[0] # first buy
        dp[0][2] = 0          # first sold out
        dp[0][3] = -prices[0] # second buy
        dp[0][4] = 0          # second sold out
        for i in range(1, n):
            dp[i][0] = dp[i - 1][0];
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i]);
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i]);
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i]);
        return dp[n-1][4];
