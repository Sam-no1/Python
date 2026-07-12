class Solution(object):
    def largestTimeFromDigits(self, arr):
        """
        :type arr: List[int]
        :rtype: str
        """
        max_t = -1
        mh = 0
        mmin = 0
        for p in itertools.permutations(arr):
            hrs = p[0]*10 + p[1]
            mm = p[2]*10 + p[3]
            if hrs < 24 and mm < 60:
                total = hrs*60 + mm
                max_t = max(max_t, total)
            mh, mmin = hrs, mmin
        if max_t == -1:
            return ""
        # return f"{max_t//60:02d}:{max_t%60:02d}"
        return "{:02d}:{:02d}".format(max_t//60, max_t%60)