# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional
from .definitions import ListNode

#! works, it is fast but is very poor memory wise
class Solution1:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return

        stack = [ListNode(head.val)]
        node = head
        while node.next:
            node = node.next
            stack.append(ListNode(node.val))

        first_node = stack.pop()
        node = first_node
        while stack:
            node.next = stack.pop()
            node = node.next

        return first_node

#! slightly better memory wise and slightly slower
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev