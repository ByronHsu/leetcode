# 思路:
#   dp[i][j]: whether s[0...i-1] matches p[0...j-1]
#   if p[j-1] != '*':
#     dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '.')
#   else:
#     dp[i][j] = dp[i][j-2] # match 0個
#                or
#     dp[i][j] = dp[i-1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.') # match 1個以上
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dp = []
        for i in range(len(s)+1):
          dp.append([])
          for j in range(len(p)+1):
            dp[i].append(False)

        dp[0][0] = True

        for j in range(1, len(p)+1):
          if p[j-1] == '*' and j-2 >= 0:
            dp[0][j] = dp[0][j-2]
            print('dp[{}][{}]={}'.format(0, j, dp[0][j]))
  

        for i in range(1, len(s)+1):
          for j in range(1, len(p)+1):
            if p[j-1] != '*':
              dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == '.')
            else:
              dp[i][j] = dp[i][j-2] or (dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.')) # match 0個 or 1個以上
            print('dp[{}][{}]={}'.format(i, j, dp[i][j]))

        return dp[len(s)][len(p)]

def test(s, p):
  print(Solution().isMatch(s, p))

if __name__ == '__main__':
  test('aab', 'c*a*b')
  test("ab", ".*")
  test("aaa","aa")
  test("",".*")