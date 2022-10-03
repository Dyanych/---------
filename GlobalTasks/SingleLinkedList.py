# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def push(self, new):
        return ListNode(new, self)
    
    def pop(self):
        return self.val, self.next


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

        #return revertIter(head) # Use Iteration
        return revertRec(head) #Use Recurtion
