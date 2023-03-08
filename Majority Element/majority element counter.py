class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element_counter = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    majority_element_counter += 1
                    output = nums[i]
        return output
