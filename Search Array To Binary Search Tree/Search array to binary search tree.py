# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None

        median = len(nums)//2
        
        root = TreeNode(nums[median])
        root.left = self.sortedArrayToBST(nums[:median])
        root.right = self.sortedArrayToBST(nums[median+1:])
        return root

