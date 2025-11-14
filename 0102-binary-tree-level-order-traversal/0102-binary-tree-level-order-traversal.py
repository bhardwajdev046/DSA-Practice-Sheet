# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=deque()
        if root is None:
            return res
        queue.append(root)
        while queue:
            level=[]
            size=len(queue)
            for i in range(size):
                e=queue.popleft()
                level.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            res.append(level)
        return res
        