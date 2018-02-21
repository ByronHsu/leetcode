# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

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