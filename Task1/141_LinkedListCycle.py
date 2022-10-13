# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        try:
            tortoise = head
            hare = head
            while tortoise or hare:
                tortoise = tortoise.next
                hare = hare.next.next
                if tortoise == hare:
                    return True
            return False
        except:
            return False