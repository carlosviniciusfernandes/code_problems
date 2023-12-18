from __future__ import annotations
from typing import Optional

class ListNode:
    """ Definition for singly-linked list. """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f'val: {self.val}, next: {self.next and self.next.val}'

    @staticmethod
    def get_list_value(head: Optional[ListNode]) -> list[int]:
        output = []
        node: ListNode = head
        while node:
            output.append(node.val)
            node = node.next

        return output

    @staticmethod
    def build_linked_list(arr: list[int]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        prev = None
        for item in arr:
            tail.next = ListNode(item)
            prev = tail
            tail = tail.next

        head = dummy.next
        return head

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
