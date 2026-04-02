# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        hash_map = {}
        i = 0
        while head!= None:
            hash_map[i] = head
            i += 1
            head = head.next
        length = i
        for k in range(length):
            if k < length//2:
                hash_map[k].next = hash_map[length-k-1]
            elif k > length//2:
                hash_map[k].next = hash_map[length-k]
            else:
                hash_map[k].next = None
        head = hash_map[0]
        #return hash_map[0]


