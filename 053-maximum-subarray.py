class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-2**32] # dummy
        ans = dp[0]
        for e in nums:
            v = max(e, e+dp[-1])
            ans = max(v, ans)
            dp.append(v)
        return ans
