# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None and head.next is None:
            return head
        
        p1 = p2 = head
        temp =None
        for i in range(n):
            p2 = p2.next

        if p2==None:
            return head.next

        while p2:
            temp = p1
            p1 = p1.next
            p2 = p2.next


        if temp:
            temp.next = p1.next
        return head