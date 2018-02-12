# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
          return 0
        dp = [1]
        for i in range(1, len(s)):
          for j in reversed(range(i-dp[i-1], i)):
            if(s[j] == s[i]):
              dp.append(i-j)
              break
          else:
            dp.append(dp[i-1]+1)
        return max(dp);

if __name__ == '__main__':
    sol = Solution()
    strs = ['abcabcbb', 'bbbbb', 'pwwkew']
    print (sol.lengthOfLongestSubstring(''))
