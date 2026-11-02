# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        # if head.next is None:
        #     return True
        # stack = [-1]
        # while head != None:
        #     if head.val == stack[-1]:
        #         stack.pop()
        #     else:
        #         stack.append(head.val)
        #     head = head.next
        
        # if stack[-1]==-1:
        #     return True
        # else:
        #     return False if len(stack)%2 != 0 else True

        temp = head
        stack = [-1]
        while temp != None:
            stack.append(temp.val)
            temp = temp.next
        
        while head != None:
            if head.val != stack.pop():
                return False
            
            head = head.next
        return True