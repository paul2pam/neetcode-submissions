# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        head = l1
        rem = 0
        while l1 and l2:
            l1.val = l2.val + l1.val  + rem

            rem = (l1.val - l1.val%10) // 10
            l1.val = int(l1.val%10)
            prev = l1
            l1 = l1.next
            l2 = l2.next

        l1 = l1 or l2
        prev.next = l1

        while l1:
            print("l1 and not l2")
            print(l1.val)
            l1.val = l1.val + rem
            rem = (l1.val - l1.val%10) // 10
            l1.val = int(l1.val%10)
            print(l1.val, rem)
            prev = l1
            l1 = l1.next

        if rem > 0:
            prev.next = ListNode(int(rem))

        return head
