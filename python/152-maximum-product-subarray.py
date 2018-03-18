class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        M, m, ans = [0]*len(nums), [0]*len(nums), 0 # 存放以nums[i]為尾的乘積和的最大/最小值
        if len(nums):
            M[0], m[0], ans = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if n >= 0:
                M[i] = max(n*M[i-1], n)
                m[i] = n*m[i-1]
            else:
                M[i] = n*m[i-1]
                m[i] = min(n*M[i-1], n)
            ans = max(ans, M[i])
        return ans
        

if __name__ == '__main__':
    Solution().maxProduct([-4,8,3,-2,3,6,-8])