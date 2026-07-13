class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        w = 0
        for i in range(len(nums)):
            print(nums)
            if nums[i] != val:
                nums[w] = nums[i]
                w+=1
        return w