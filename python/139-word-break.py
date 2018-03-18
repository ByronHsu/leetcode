
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        b = [False]*(len(s)+1)
        b[0] = True
        s = '#'+s
        for i in range(1, len(s)):
            for w in wordDict:
                prev = i-len(w)
                if prev >= 0 and b[prev] == True and s[prev+1:i+1] == w:
                    b[i] = True
                    break
        return b[len(s)-1]

if __name__ == '__main__':
    Solution().wordBreak('aaaaa',['aa', 'aaa'])