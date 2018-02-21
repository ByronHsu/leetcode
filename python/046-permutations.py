# Given a collection of distinct numbers, return all possible permutations.

# For example,
# [1,2,3] have the following permutations:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(rest, cum):
            if len(rest) == 0:
                ans.append(cum)
            for e in rest:
                tr = rest.copy()
                tr.remove(e)
                tc = cum.copy()
                tc.append(e)
                dfs(tr, tc)

        dfs(nums.copy(), [])
        return ans

def test(L):
    print(Solution().permute(L))

if __name__ == '__main__':
    test([1,2,3])
        