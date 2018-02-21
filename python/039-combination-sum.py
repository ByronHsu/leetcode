class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(L, idx, cum):
            if cum > target:
                return
            if cum == target:
                ans.append(L)
                return
            for i in range(idx, len(candidates)):
                tmp = L.copy()
                tmp.append(candidates[i])
                dfs(tmp, i, cum+candidates[i])

        dfs([], 0, 0)
        return ans

def test(L, tar):
    print(Solution().combinationSum(L, tar))

if __name__ == '__main__':
    test([2, 3, 6, 7], 7)
    