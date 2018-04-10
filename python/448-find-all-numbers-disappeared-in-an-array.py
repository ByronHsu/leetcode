class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1 2 3 4 5 6
        # 0 1 2 3 4 5
        for n in nums:
            if nums[abs(n) - 1] > 0:
                nums[abs(n) - 1] = -nums[abs(n) - 1]
        ans = []
        for i in range(1, len(nums)+1):
            if nums[i - 1] > 0:
                ans.append(i)
        return ans