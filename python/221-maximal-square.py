class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        for i in range(len(matrix)):
            matrix[i].append(0)
            matrix[i].insert(0, 0)
        matrix.insert(0, [0]*len(matrix[0]))
        matrix.append([0]*len(matrix[0]))
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j])+1
                ans = max(ans, dp[i][j])
        return ans*ans