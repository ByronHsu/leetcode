class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = {}
        nums.insert(0, 0)
        dic[0] = 1
        count = 0
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] # sum from index = 0
            target = nums[i]-k
            if target in dic: 
                count += dic[target]
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1

        return count
        