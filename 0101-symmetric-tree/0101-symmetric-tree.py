# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def helper(self,r1,r2):
    #     if r1 is None and r2 is None:
    #         return True
    #     if r1 is None or r2 is None:
    #         return False
    #     if r1.val != r2.val:
    #         return False
    #     left = self.helper(r1.left ,r2.right)
    #     right = self.helper(r1.right ,r2.left)
            
    #     return left and right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue=deque([(root.left,root.right)])

        while queue:
            e1,e2=queue.popleft()
            if not e1 and not e2:
                continue
            if not e1 or not e2:
                return False
            if e1.val!=e2.val:
                return False
            queue.append((e1.left,e2.right))
            queue.append((e1.right,e2.left))
            
        return True
