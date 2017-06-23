"""
You’re given the pointer to the head node of a doubly linked list. Reverse the
order of the nodes in the list. The head node might be NULL to indicate that the
list is empty.

Input Format
You have to complete the Node* Reverse(Node* head) method which takes one
argument - the head of the doubly linked list. You should NOT read any input
from stdin/console.

Output Format
Change the next and prev pointers of all the nodes so that the direction of the
list is reversed. Then return the head node of the reversed list. Do NOT print
anything to stdout/console.

"""


class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def Reverse(head):
    if not head:
        return head

    while head:
        head.next, head.prev = head.prev, head.next
        if not head.prev:
            return head
        head = head.prev
