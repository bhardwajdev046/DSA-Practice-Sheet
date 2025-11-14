# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # if root is None:
        #     return 0
        # if root.right is None:
        #     return 1+self.minDepth(root.left)
        # if root.left is None:
        #     return 1+self.minDepth(root.right)
        # return 1 + min(self.minDepth(root.left),self.minDepth(root.right))
        queue=deque([root])
        depth=1
        if root is None:
            return 0
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth+=1
        return depth
            