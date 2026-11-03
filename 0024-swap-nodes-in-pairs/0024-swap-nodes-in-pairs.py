# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        # p1 = head
        # p2 = head.next

        # while p2 and p2.next:
        #     temp = p1.val
        #     p1.val = p2.val
        #     p2.val = temp

        #     p1 = p1.next.next
        #     p2 = p2.next.next
        # if p2:
        #     temp = p1.val
        #     p1.val = p2.val
        #     p2.val = temp
        
        # return head

        p1 = temp = head
        p2 = head.next
        dummy = ListNode(0,head)
        d_h = dummy

        while p1 and p2:
            p1.next = p2.next
            p2.next = p1

            dummy.next = p2
            dummy = p1

            p1 = p1.next
            if p1 and p1.next:
                p2 = p1.next
            else:
                break
            

        return d_h.next