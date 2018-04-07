class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # dp[i][s]: i個前和為s的組合數
        # dp[i][s] = dp[i-1][s-a[i]] + dp[i-1][s+a[i]]
        N = len(nums)
        nums.insert(0, 0) # dummy
        Sum = sum(nums)
        if S > Sum or S < -Sum: return 0
        offset = Sum
        # -3 -2 -1 0 1 2 3
        dp = [[0]*(2*Sum + 1) for _ in range(len(nums)+1)]
        dp[0][0+offset] = 1
        for i in range(1, N+1):
            for j in range(Sum, -Sum-1, -1):
                if dp[i-1][j+offset] != 0:
                    dp[i][j+nums[i]+offset] += dp[i-1][j+offset]
                    dp[i][j-nums[i]+offset] += dp[i-1][j+offset]
        return dp[N][S+offset]