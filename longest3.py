class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        word = ""
        ch = ""
        for i in range(len(s)):
            if s[i] not in ch:
                ch += s[i]
            else:
                dup = ch.index(s[i])
                ch = ch[dup+1:]+s[i]
            if len(ch) > len(word):
                word = ch
        return len(word)
