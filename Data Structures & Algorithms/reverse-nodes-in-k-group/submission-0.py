# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        res = ListNode(0)
        prev = res
        curr = head
        tail = None
        index = 0

        while curr:
            tail = curr

            while curr and index < k:
                curr = curr.next
                index +=1
            
            if index >= k:
                index = 0
                prev.next = self.reverse(tail, k)
                prev = tail
            else:
                prev.next = tail
        return res.next


    def reverse(self, head, k):
        prev = None
        curr = head

        while curr and k > 0:
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node
            k -=1
        return prev
