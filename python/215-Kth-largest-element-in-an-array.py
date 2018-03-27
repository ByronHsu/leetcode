from queue import PriorityQueue
# 維護一個大小為k的pq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pq = PriorityQueue()
        for i in range(k):
            print(pq.queue)
            pq.put(nums[i])
        for i in range(k, len(nums)):
            print(pq.queue)
            if nums[i] > pq.queue[0]:
                pq.get()
                pq.put(nums[i])

        return pq.queue[0]

if __name__ == '__main__':
    Solution().findKthLargest([3,4,2,5,1], 3)