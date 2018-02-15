class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        book = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'], '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}
        ans = []
        def dfs(index, s):
          if index == len(digits):
            if len(s) > 0:
              ans.append(s)
            return
          if digits[index] not in book:
            dfs(index + 1, s)
          else:
            for i in book[digits[index]]:
              dfs(index + 1, s + i)
        
        dfs(0, '')
        print(ans)
        return ans
def test(s):
  print('input: {}'.format(s))
  print('ans: {}'.format(Solution().letterCombinations(s)))

if __name__ == '__main__':
  test('123')