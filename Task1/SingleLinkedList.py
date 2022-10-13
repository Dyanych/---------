from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def __str__(self) -> str:
        tmpStr = ''
        while self.next:
            tmpStr += str(self.val) + ' -> '
            self = self.next
        tmpStr += str(self.val) + ' -> Null'
        return tmpStr
    
    def push(self, new):
        return ListNode(new, self)
    
    def pop(self):
        try:
            return self.val, self.next
        except: # If List is empty
            return None, None

class Solution:        
    def reverseList(self, head: ListNode) -> ListNode:
        def revertIter(current: ListNode):
            final = None

            while current:
                temporary = current.next
                current.next = final
                final = current
                current = temporary

            return final

        def revertRec(current, final = None):
            if current:
                return final
            temporary = current.next
            current.next = final
            final = current
            current = temporary
            return revertRec(current, final)

        return revertRec(head)
        
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

a = Solution()

tmpList5 = ListNode(5)
tmpList4 = ListNode(4, tmpList5)
tmpList3 = ListNode(3, tmpList4)
tmpList2 = ListNode(2, tmpList3)
tmpList1 = ListNode(1, tmpList2)
print(tmpList1)
print(tmpList1.pop())

        

