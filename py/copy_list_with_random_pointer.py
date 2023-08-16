from typing import Optional


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        prev = None
        node = head
        new_head_node = None
        while node:
            new_node = Node(node.val)
            if not new_head_node:
                new_head_node = new_node
            node.new_node = new_node
            if prev:
                prev.next = new_node
            node = node.next
            prev = new_node

        node = head
        while node:
            random_node = node.random
            if random_node:
                node.new_node.random = random_node.new_node
            node = node.next

        return new_head_node


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
