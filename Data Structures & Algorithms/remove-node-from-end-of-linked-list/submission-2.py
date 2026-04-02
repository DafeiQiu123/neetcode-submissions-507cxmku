# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            fast = fast.next
        pre = None
        while fast != None:
            pre = slow
            slow = slow.next
            fast = fast.next
        if pre == None:
            return head.next
        pre.next = pre.next.next
        return head