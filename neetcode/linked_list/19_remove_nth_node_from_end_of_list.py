# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from .definitions import ListNode

class Solution:

    @staticmethod
    def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next


testCases = [
    ({'head':[1,2,3,4,5], 'n':2}, [1,2,3,5]),
    ({'head':[1], 'n':1}, []),
    ({'head':[1,2], 'n':1}, [1]),
]
for case in testCases:
    input, expected = case
    head = ListNode.build_linked_list(input['head'])
    newHead = Solution.removeNthFromEnd(head, input['n'])
    assert ListNode.get_list_value(newHead) == expected

























