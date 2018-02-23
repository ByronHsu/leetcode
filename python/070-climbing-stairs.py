class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0]*(n+1)
        for i in range(n+1):
            if i == 0 or i == 1:
                dp[i] = 1
            else:
                dp[i] = dp[i-1]+dp[i-2]
        return dp[n]
