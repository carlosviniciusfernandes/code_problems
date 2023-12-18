# https://leetcode.com/problems/reorder-list/

from typing import Optional
from .definitions import ListNode

class Solution:

    @staticmethod
    def reorderList(head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next # two pointers in the key here
        # transverse the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        # reverse second half
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2




if __name__ == '__main__':
    testCases = [
        ([1,2,3,4,5], [1,5,2,4,3]),
        ([1,2,3,4], [1,4,2,3]),
    ]
    for case in testCases:
        input, expected = case
        head = ListNode.build_linked_list(input)
        Solution.reorderList(head)
        assert ListNode.get_list_value(head) == expected
