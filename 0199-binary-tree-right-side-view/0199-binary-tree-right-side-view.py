# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        q = deque([root])
        res = []
        while q:
            n=len(q)
            for i in range(n):
                e = q.popleft()
                if n-i ==1:
                    res.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        return res