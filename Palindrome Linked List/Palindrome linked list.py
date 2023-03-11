# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        final_value = []
        if not head:
            return None
        while head:
            final_value.append(head.val)
            head = head.next
        return final_value == final_value[::-1]
