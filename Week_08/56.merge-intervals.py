class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        思路：排序后遍历，依次取合并重叠区间。
        """

        intervals.sort()
        intervals = collections.deque(intervals)
        res = [intervals.popleft()]
        while intervals:
            pre = res[-1]
            temp = intervals.popleft()
            if pre[-1] >= temp[0]:
                res[-1] = [pre[0], max(pre[-1], temp[-1])]
            else:
                res.append(temp)
        return res
            