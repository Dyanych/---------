# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverseList(self, head: ListNode) -> ListNode:
    def revert(current: ListNode):
        temporary, final = None, None

        while current:
            temporary = current.next
            current.next = final
            final = current
            current = temporary

        return final
    return revert(head)
