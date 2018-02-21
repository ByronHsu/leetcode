class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        def dfs(cnt, s, buf):
          if len(buf) == 0:
            ans.append(s)
            return
          if '(' in buf:
            tmp = buf.copy()
            tmp.remove('(')
            tmp.append(')')
            dfs(cnt + 1, s + '(', tmp)
          if ')' in buf:
            tmp = buf.copy()
            tmp.remove(')')
            dfs(cnt + 1, s + ')', tmp)

        dfs(0, '', ['(']*n)

        # print(ans)
        return ans

def test(n):
  print(Solution().generateParenthesis(n))

if __name__ == '__main__':
  test(2)