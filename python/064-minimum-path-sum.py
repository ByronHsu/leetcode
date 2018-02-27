class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), 0
        if m > 0:
            n = len(grid[0])

        dp = [[0 for i in range(n)]for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i][j-1],dp[i-1][j])+grid[i][j]
                elif i <= 0 and j > 0:
                    dp[i][j] = dp[i][j-1]+grid[i][j]
                elif i > 0 and j <= 0:
                    dp[i][j] = dp[i-1][j]+grid[i][j]
                elif i <= 0 and j <= 0:
                    dp[i][j] = grid[i][j]
                print('dp[{}][{}]={}'.format(i,j,dp[i][j]))
        print(dp[m-1][n-1])
        return dp[m-1][n-1]

if __name__ == '__main__':
    Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]])

# 131
# 151
# 421