# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverseOneGroup(head, tail):
            tail.next = None

            prev = None
            curr = head

            while curr: 
                nxt = curr.next

                curr.next = prev

                prev = curr
                curr = nxt

            return tail, head

        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        passes = length // k
        curr = head

        headswapped = False
        prevtail = None
        for i in range(passes):
            
            tmphead = curr
            for _ in range(k - 1):
                curr = curr.next
            tmp = curr.next
            tmptail = curr

            newhead, newtail = reverseOneGroup(tmphead, tmptail)
            if not headswapped:
                head = newhead
                headswapped = True
            if prevtail:
                prevtail.next = newhead
            print(newhead.val, newtail.val)
            curr = tmp
            newtail.next = curr
            prevtail = newtail
        
        return head
