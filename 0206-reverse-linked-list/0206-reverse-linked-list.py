# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        p1 = None
        p2 = temp = head
        while p2 != None:
            p2 = p2.next
            temp.next = p1

            p1 = temp
            temp = p2
        return p1