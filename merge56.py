class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for cur in intervals[1:]:
            last_merged = merged[-1]
            if cur[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], cur[1])
            else:
                merged.append(cur)
        return merged