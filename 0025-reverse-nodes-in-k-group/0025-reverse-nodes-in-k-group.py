# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            prev = end
            while start.next != end:
                nextStart = start.next
                start.next = prev
                prev = start
                start = nextStart
            start.next = prev
            return start

        dummy = ListNode(next=head)
        head = dummy
        while head and head.next:
            tail = head.next
            count = k
            while tail and count > 0:
                tail = tail.next
                count -= 1
            if count != 0:
                break
            nextHead = head.next
            head.next = reverse(head.next, tail)
            head = nextHead
        return dummy.next