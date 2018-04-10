class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1 2 3 4 5 6
        # 0 1 2 3 4 5
        ans = []
        for n in nums:
            nums[abs(n) - 1] = -nums[abs(n) - 1]
            if nums[abs(n) - 1] > 0:
                ans.append(abs(n))
        return ans
        