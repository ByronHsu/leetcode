class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(i, cum):
            if i >= len(nums):
                ans.append(cum)
                return
            if i == -1:
                dfs(i+1, cum.copy())
            else:
                tmp1 = cum.copy()
                tmp1.append(nums[i])
                dfs(i+1, tmp1)
                dfs(i+1, cum.copy())
        dfs(-1, [])
        return ans

if __name__ == '__main__':
    print(Solution().subsets([1,2,3]))