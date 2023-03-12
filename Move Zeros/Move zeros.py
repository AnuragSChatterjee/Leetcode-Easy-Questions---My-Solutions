class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[x] = nums[x], nums[i]
                i+=1
                x+=1
        return nums
                
            