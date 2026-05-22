# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next and head.next.next == head:
            return True

        s = set()
        curr = head
        while (curr):
            if curr in s:
                return True
            s.add(curr)
            
            if (curr.next):
                print(s, curr.val, curr.next.val)
            else: 
                print(s, curr.val)
            curr = curr.next
           
            
        return False