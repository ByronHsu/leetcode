# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:

# Input: "babad"

# Output: "bab"

# Note: "aba" is also a valid answer.
 

# Example:

# Input: "cbbd"

# Output: "bb"

class Solution:
    # 思路:
    # 把char倆倆之間插入'.', 在頭尾補dummy以避免邊界計算
    # C: center, R = C + P[i]
    # if i < R:
    #   P[i] = min(R - i, P[2 * C - i])
    # 往外擴展
    # while(s[i + P[i] + 1] == s[i - P[i] - 1]):
    #   P[i] += 1
    # 擴展成功 換center
    # if i + P[i] > R:
    #     C, R = i, i + P[i]
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        T = '#'.join('!{}%'.format(s))
        C, R = 0, 0
        P = []
        for i in range(len(T)):
          P.append(0)
        
        for i in range(1, len(T)-1):
          if i < R:
            P[i] = min(R - i, P[2 * C - i])
          while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1
          if i + P[i] > R:
            C, R = i, i + P[i]
        radius, index = max((n, i) for i, n in enumerate(P))
        return s[(index  - radius)//2: (index + radius)//2]

    def longestPalindrome_TLE(self, s):
        """
        :type s: str
        :rtype: str
        """
        p = []
        for i in range(len(s)):
          p.append([])
          for j in range(len(s)):
            p[i].append(False)
        
        ans = ''
        
        for i in range(len(s)):
          for j in range(len(s)):
            if j + i >= len(s):
              break
            if j == j + i:
              p[j][j + i] = True
            elif i == 1:
              if s[j] == s[j + i]:
                p[j][j + i] = True
              else:
                p[j][j + i] = False
            else:
              p[j][j + i] = (p[j + 1][j + i - 1] and s[j] == s[j + i])
            
            if p[j][j + i]:
              ans = s[j:j + i + 1]

        return ans

def test(s):
  print('input: {}'.format(s))
  print('ans: {}'.format(Solution().longestPalindrome(s)))

if __name__ == '__main__':
  test('bananas')
  test('acdbdacdbebdca')
  test('babad')
  test('cbbd')
  test('ccc')