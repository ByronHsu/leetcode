# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

# For "(()", the longest valid parentheses substring is "()", which has length = 2.

# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

# Smart way:
#   看匹配完之後index的差值
class Solution:
    def longestValidParentheses(self, s):
      s = ')' + s + '('
      L, I = [], []
      M = 0
      for i, c in enumerate(s):
        if c == ')':
          if len(L) and L[-1] == '(':
            L.pop()
            I.pop()
          else:
            L.append(')')
            I.append(i)
        elif c == '(':
          L.append('(')
          I.append(i)

      for i in range(1, len(I)):
        M = max(I[i]-I[i-1]-1, M)
      return M
        
    def longestValidParentheses_byron(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = []
        for c in s:
          if c == ')':
            if len(L) > 1 and isinstance(L[-1],int) == True and L[-2] == '(':
              cum = L[-1] + 2
              L[-2] = cum
              L.pop()
            elif len(L) and L[-1] == '(':
              L[-1] = 2
            else:
              L.append(')')
          else:
            L.append('(')
          if len(L) > 1 and isinstance(L[-1],int) == True and isinstance(L[-2],int) == True:
            L[-2] = L[-1] + L[-2]
            L.pop()
          print(L)

        L = [x for x in L if isinstance(x,int) == True]
        res = 0
        if len(L):
          res = max(max(L), res) 

        return res

def test(s):
  print(Solution().longestValidParentheses(s))

if __name__ == '__main__':
  # test(')))()())()())))())')
  # test('')
  # test('()')
  # test('()(()')
  # test("())")
  test(")()(((())))(")
  # test("(()(((()")
  # test("")