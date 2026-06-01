# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        curr = list1
        curr2 = list2
        if (list1.val > list2.val):
            curr, curr2 = curr2, curr
        
        head = curr
        
        while curr:
            if not curr.next:
                if curr2:
                    curr.next = curr2
                break
            if not curr2:
                break
            if curr2.val < curr.next.val:
                tmp = curr.next
                curr.next = curr2
                curr2 = curr2.next
                curr.next.next = tmp
            curr = curr.next
            
        return head