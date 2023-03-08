class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = 0
        for i in nums:
            output ^= i
        return output