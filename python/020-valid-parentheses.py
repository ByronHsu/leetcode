class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        L = []
        for c in s:
          # print(L)
          if len(L) and c == ')' and L[-1] == '(':
            L.pop()
          elif len(L) and c == ']' and L[-1] == '[':
            L.pop()
          elif len(L) and c == '}' and L[-1] == '{':
            L.pop()
          else:
            L.append(c)

        if len(L):
          return False
        else:
          return True
            

def test(s):
  print(Solution().isValid(s))

if __name__ == '__main__':
  # test('(())')
  test('()[]{}')