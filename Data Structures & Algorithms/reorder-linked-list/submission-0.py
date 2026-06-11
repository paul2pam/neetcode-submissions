# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None
        #we've split it down the middle

        curr = head2
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            

        head2 = prev
        #second part of linked list is reversed 
        
        curr1 = head
        curr2 = head2
        
        while curr1 and curr2:
            tmp1 = curr1.next
            tmp2 = curr2.next
            curr1.next = curr2
            curr2.next = tmp1

            curr1 = tmp1
            curr2 = tmp2
            
        
