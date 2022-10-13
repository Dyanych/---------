# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            hare = head
            while hare.next or hare.next.next:
                head = head.next
                hare = hare.next.next
            else:
                return head.next
        except:
            return head

a = Solution()
print(a.middleNode([1,2,3,4,5]))