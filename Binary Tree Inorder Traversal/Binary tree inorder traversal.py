# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        final_answer = []
        if not root:
            return None
        def treetraversal(treenode):
            if not treenode:
                return None
            treetraversal(treenode.left)
            final_answer.append(treenode.val)
            treetraversal(treenode.right) 
        treetraversal(root)  
        return final_answer
        