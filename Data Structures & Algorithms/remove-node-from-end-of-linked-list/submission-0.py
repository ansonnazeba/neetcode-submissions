# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ll_len = 0

        curr = head
        while curr:
            ll_len += 1
            curr = curr.next
        
        n = ll_len - n + 1 # position of the node to be removed
        print(n)
        if n == 1:
            return head.next

        i = 1
        curr = head
        while curr.next:
            if i + 1 == n:
                curr.next = curr.next.next
                break
            i += 1
            curr = curr.next
        
        return head

        



        