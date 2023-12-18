# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


from .definitions import ListNode


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode() #! prior to first element, dummy.next will be the first element
        tail = dummy

        while list1 and list2:
            #! we are no iterating per say, more like "poping" the lists until one of them becomes None
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next #! tail becomes the next member during looping

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next