class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(1)
        nums.insert(len(sums)-1, 1)
        ans = 0
        def dfs(List, Sum):
            if len(List) == 2:
                ans = max(ans, Sum)
            for i in range(1, len(List)-1):
                tmp = []
                for j in range(1, len(List)-1):
                    if i != j:
                        tmp.push(List)
                cur = List[i-1]*List[i]*List[i+1]
                dfs(tmp, Sum+cur)

        return ans