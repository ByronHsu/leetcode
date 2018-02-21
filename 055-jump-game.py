class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        r = 0
        for i in range(len(nums)):
            if i <= r:
                if i == len(nums)-1:
                    return True
                r = max(nums[i]+i, r)
            else:
                return False
        
        return False