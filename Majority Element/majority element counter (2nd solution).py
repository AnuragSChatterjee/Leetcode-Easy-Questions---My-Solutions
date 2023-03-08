from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) / 2
        majority_element_counter = Counter(nums)
        for i in range(0, len(nums)):
            if Counter(nums) > length:
                return nums[i]
