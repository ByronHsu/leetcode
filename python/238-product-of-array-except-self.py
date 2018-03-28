class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p, n = 1, len(nums)
        output = []
        for i in range(n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1, -1, -1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output