# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        res_ptr = res

        while list1 and list2:
            if list1.val > list2.val:
                res_ptr.next = list2
                list2 = list2.next
            elif list1.val <= list2.val:
                res_ptr.next = list1
                list1 = list1.next
            res_ptr = res_ptr.next
        if not list1 and list2:
            res_ptr.next = list2
        if not list2 and list1:
            res_ptr.next = list1
        return res.next