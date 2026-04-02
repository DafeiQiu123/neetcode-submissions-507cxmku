# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False  # No cycle if the list is empty or has only one node
        
        p1 = head  # Slow pointer
        p2 = head  # Fast pointer
        
        while p2 and p2.next:
            p1 = p1.next            # Move slow pointer by 1 step
            p2 = p2.next.next       # Move fast pointer by 2 steps
            
            if p1 == p2:
                return True         # Cycle detected
        
        return False                # No cycle