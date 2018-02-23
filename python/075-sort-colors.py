class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        cnt = [0]*3
        for i in nums:
            if i == 0:
                cnt[0] += 1
            elif i == 1:
                cnt[1] += 1
            elif i == 2:
                cnt[2] += 1
        print(cnt)
        idx = 0
        for i in range(len(nums)):
            while cnt[idx] == 0:
                idx += 1
            nums[i] = idx
            cnt[idx] -= 1
        print(nums)

if __name__ == '__main__':
    print(Solution().sortColors([2,0]))