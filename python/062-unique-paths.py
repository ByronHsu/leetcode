class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+2)] for __ in range(m+2)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if (i, j) == (1, 1):
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m][n]
if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))