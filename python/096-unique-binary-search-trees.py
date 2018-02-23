class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[n] = dp[0]*dp[n-1] + dp[1]*dp[n-2] + ... dp[n-1]*dp[0]
        dp = [0]*(n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]
    def numTrees_rec(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [[False for i in range(n)] for j in range(n)]
        def dfs(left, right, x):
            if dp[len(left)][len(right)] != False:
                return dp[len(left)][len(right)]
            lcum, rcum = 0, 0
            if len(left) == 0:
                lcum = 1
            if len(right) == 0:
                rcum = 1
            for i in range(len(left)):
                lcum += dfs(left[:i].copy(), left[i+1:].copy(), left[i])
            for i in range(len(right)):
                rcum += dfs(right[:i].copy(), right[i+1:].copy(), right[i])
            dp[len(left)][len(right)] = lcum*rcum
            return lcum*rcum
            
        L = list(range(1, n+1))
        cum = 0
        for i in range(len(L)):
            l, r = L[:i].copy(), L[i+1:].copy()
            cum += dfs(l, r, L[i])
        return cum


def test(n):
    print(Solution().numTrees(n))
if __name__ == '__main__':
    test(12)

    #    10
    #   9  11
# dp[0][0] = 1
# dp[0][1] = 1
# dp[0][2] = (1)*(dp[0][1]+dp[1][0])
# dp[0][3] = (1)*(dp[0][2]+dp[1][1]+dp[2][0])
# dp[i][j] = (dp[0][i-1]+...dp[i-1][0])*(dp[0][j-1]+...dp[j-1][0])     