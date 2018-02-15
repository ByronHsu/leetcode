# Two Sum
class Solution:
   def twoSum(self, nums, target):
      """
      :type nums: List[int]
      :type target: int
      :rtype: List[int]
      """
      dic = {}
      for i in range(len(nums)):
         dic[nums[i]] = i
      for i in range(len(nums)):
         if target - nums[i] in dic:
            if(dic[target-nums[i]] != i):
               return [i, dic[target-nums[i]]]


s = Solution()
print(s.twoSum([3,2,4], 6))
# print s.twoSum([2, 7, 11, 15], 9)
