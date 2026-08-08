# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         m=len(lists)
#         heap=[]
#         if m==0 :
#             return []
#         ans=[]
#         for row in range(m):
#             heapq.heappush(lists[row][0],row,0)
#         while heap:
#             val,row,col=heapq.heappop(heap)
#             ans.append(val)
#             if col<len(lists[row]):
#                 heapq.heappush(heap,lists[row][col+1],row,col+1)
#         return ans

import heapq

class Solution:
    def mergeKLists(self, lists):

        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy.next