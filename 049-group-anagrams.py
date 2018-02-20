# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in d:
                d[ss] = [s]
            else:
                d[ss].append(s)
        ans = []
        for key in d:
            ans.append(d[key])
        return ans

def test(strs):
    print(Solution().groupAnagrams(strs))

if __name__ == '__main__':
    test(["eat", "tea", "tan", "ate", "nat", "bat"])
        