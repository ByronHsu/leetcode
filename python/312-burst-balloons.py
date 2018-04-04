class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
        for i in range(1, n + 1): # 1 to n
            for left in range(1, n - i + 2): # 1 to n - i + 1
                right = left + i - 1
                for j in range(left, right + 1): # left to right
                    burst = dp[left][j - 1] + nums[left - 1]*nums[j]*nums[right + 1] + dp[j + 1][right] # last burst balloon
                    dp[left][right] = max(dp[left][right], burst)
                # print('dp[{}][{}] = {}'.format(left, right, dp[left][right]))
        return dp[1][n]