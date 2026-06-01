# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        n = len(lists)
        heads = [0] * n
        for i in range(n):
            heads[i] = lists[i]
            
        curr = None
        for i, head in enumerate(heads): 
            if curr is None and head is not None:
                curr = heads[i]
            if head.val < curr.val:
                curr = head
        res = curr
        #print(f"curr: {curr.val}")

        while curr:     
            nxt = None
            i_to_increment = 0
            for i, head in enumerate(heads):
                if head:
                    #print(f"heads[{i}] is {head.val}")
                    if nxt is None or head.val < nxt.val:
                        nxt = heads[i]
                        i_to_increment = i
            if heads[i_to_increment]:
                heads[i_to_increment] = heads[i_to_increment].next
            #if nxt:            
                #print(f"nxt is {nxt.val}")
            curr.next = nxt
            curr = nxt
            
        return res
        