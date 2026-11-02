# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        cnt = 0
        if head is None or k==0:
            return head
        temp = head
        while temp is not None:
            cnt+=1
            temp = temp.next

        temp = head
        k = k % cnt
        if k == 0:
            return head

        steps = cnt-k
        while steps-1:
            temp = temp.next
            steps-=1
        dummy = temp.next
        temp.next = None

        temp = dummy
        while dummy.next != None:
            dummy = dummy.next
        dummy.next = head

        return temp


