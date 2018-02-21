# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# 思路:
#   將每個數字取出, 用和0的差值做2sum, 使用2 pointers的方法
#   要把重複的判斷否則會tle
#   重要優化: 如果第一個>0 直接掰掰

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(now, value):
            l, r = now + 1, len(nums) - 1
            lu, ru = False, False
            ret = []
            while l < r:
              if nums[l] + nums[r] > value:
                r = r - 1
                ru = True
              elif nums[l] + nums[r] < value:
                l += 1
                lu = True
              elif nums[l] + nums[r] == value:
                tmp = [nums[now], nums[l], nums[r]]
                ans.append(tmp)
                r, l = r - 1, l + 1
                ru, lu = True, True

              if lu:
                while l < r and nums[l] == nums[l - 1]:
                  l += 1
              if ru:
                while l < r and nums[r] == nums[r + 1]:
                  r -= 1

              lu, ru = False, False
            
        ans = []
        nums.sort()

        i = 0
        while i < len(nums):
          if(nums[i] > 0):
            break
          twoSum(i, 0 - nums[i])
          i += 1
          while i < len(nums) and nums[i] == nums[i - 1]:
            i += 1

        return ans



def test(L):
  print('input: {}'.format(L))
  print('ans: {}'.format(Solution().threeSum(L)))

if __name__ == '__main__':
  test([-1, 0, 1, 2, -1, -4])
  test([-1,0,1,2,-1,-4])
  test([-2,0,0,2,2])
