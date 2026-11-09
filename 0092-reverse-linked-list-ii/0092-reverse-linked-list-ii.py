# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        # if head is None or head.next is None:
        #     return head
        # curr = p2 = head
        # p1 = None
        # remain = left

        # while left != 0:
        #     p1 = curr
        #     curr = curr.next
        #     p2 = curr
        #     left-=1

        # while p2 :
        #     p2 = p2.next
        #     curr.next = p1
        #     p1.next = None

        #     p1 = curr
        #     curr = p2
        #     right-=1
        # print(p1)
        # return p2

        if head is None and head.next is None:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        head = dummy

        l1 = dummy
        curr = head
        remain = left

        while remain:
            l1 = curr
            curr = curr.next
            remain -= 1
        
        p1 = None
        temp = curr
        for i in range(right-left+1):
            p2 = curr.next
            curr.next = p1
            p1 = curr
            curr = p2
        l1.next = p1

        temp.next = curr
        return dummy.next