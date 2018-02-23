# 先把他依照左界排序好
# 接著一個個放到stack中 檢查和top有沒有重疊, 有的話就merge
# 為什麼需要檢查跟top就好 他不會一直merge下去嗎?
# [G1][G2]X
# 不會
# 因為從G2開始已經完全跟G1隔離了 不可能再有merge的機會
# 而且因為是依照start排序的 所以X.start一定大於G2.start 不會有跨越到G1的機會
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda i: i.start)  # sorts in place
        s = []
        for e in intervals:
            if len(s) and e.start <= s[-1].end:
                s[-1].end = max(s[-1].end, e.end)
            else:
                s.append(e)
        # print([(i.start, i.end) for i in s]);
        return s

def L2I(intervals):
    L = []
    for i in intervals:
        L.append(Interval(i[0],i[1]))
    return L

if __name__ == '__main__':
    I = L2I([[1,3],[2,6],[15,18],[8,10]])
    print(Solution().merge(I))