class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_s = "".join(sorted(s))
        s_t = "".join(sorted(t))
        if s_s == s_t:
            return True
        return False