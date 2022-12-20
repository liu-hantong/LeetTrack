# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        while cur.next and cur.next.next:
            tail = cur.next.next
            cur.next.next = cur.next.next.next
            tail.next = cur.next
            cur.next = tail
            cur = cur.next.next
        return dummy.next