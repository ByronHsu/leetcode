class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # dp[n][s]: 第n種錢 總和為s 所能使用的最小硬幣數
        N, S = len(coins), amount
        dp = [2**32] * (S+1)
        dp[0] = 0
        for i in range(1, N+1):
            for j in range(S+1):
                if j >= coins[i-1]: dp[j] = min(dp[j-coins[i-1]]+1, dp[j])
        if dp[S] == 2**32: return -1
        else: return dp[S]