class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        check = {}
        for i, num in enumerate(nums):
            comp = target-num
            if comp in check:
                return [check[comp], i]
            check[num] = i
                
            
