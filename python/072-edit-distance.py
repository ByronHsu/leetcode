class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1, l2 = len(word1), len(word2)
        dp = [[0 for i in range(l2+1)] for j in range(l1+1)]
        for i in range(l1+1):
            for j in range(l2+1):
                if i == 0:
                    dp[i][j] = j
                elif j == 0:
                    dp[i][j] = i
                else:
                    dp[i][j] = min(dp[i-1][j-1]+(word1[i-1] != word2[j-1]), dp[i-1][j]+1, dp[i][j-1]+1)
        return dp[l1][l2]

if __name__ == '__main__':
    Solution().minDistance('abc', 'ab')