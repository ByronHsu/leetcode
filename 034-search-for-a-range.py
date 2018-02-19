import math
class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def bsl():
            l, r = 0, len(nums)-1
            while(l < r):
                mid = math.floor((l+r)/2)
                if nums[mid] >= target:
                    r = mid
                if nums[mid] < target:
                    l = mid+1
            if len(nums) == 0 or nums[l] != target:
                return -1
            else:
                return l
        def bsr():
            l, r = 0, len(nums)-1
            while(l < r):
                mid = math.ceil((l+r)/2)
                if nums[mid] > target:
                    r = mid-1
                if nums[mid] <= target:
                    l = mid
            if len(nums) == 0 or nums[l] != target:
                return -1
            else:
                return l
        return [bsl(), bsr()]

def test(nums, target):
    print(Solution().searchRange(nums, target))
if __name__ == '__main__':
    test([5, 7, 7, 8, 8, 10], 11)
