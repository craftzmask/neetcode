# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        
        stack = []
        while cur:
            stack.append(cur)
            cur = cur.next

        cur = head
        for i in range(len(stack) // 2):
            tail = stack.pop()
            next = cur.next
            tail.next = next
            cur.next = tail
            cur = next

        cur.next = None
        
        return head