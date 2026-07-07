class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        sl = list(s)
        sl = sorted(sl)
        tl = list(t)
        tl = sorted(tl)
        for i in range(len(s)):
            if sl[i] != tl[i]:
                return False
        return True
        