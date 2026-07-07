from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramdic = defaultdict(list)
        for s in strs:
            sorted_w = "".join(sorted(s))
            anagramdic[sorted_w].append(s)
        return list(anagramdic.values())