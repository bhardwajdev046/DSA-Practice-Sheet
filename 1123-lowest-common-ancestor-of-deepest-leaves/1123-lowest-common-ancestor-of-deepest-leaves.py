# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def levelorder(root):
            queue = deque()
            if root is None:
                return None
            queue.append(root)
            while queue:
                leaf = []
                for i in range(len(queue)):
                    e = queue.popleft()
                    leaf.append(e)
                    if e.left:
                        queue.append(e.left)
                    if e.right:
                        queue.append(e.right)                  
            return leaf
        
        def LCA(root, p, q):
            if root is None:
                return None
            if root == p or root == q:
                return root
            left = LCA(root.left, p, q)
            right = LCA(root.right, p, q)

            if left is not None and right is not None:
                return root
            if left is not None:
                return left
            return right
        
        deepest = levelorder(root)
        if not deepest:
            return None
        # Sab deepest leaves ka common LCA
        lca = deepest[0]
        for i in range(1, len(deepest)):
            lca = LCA(root, lca, deepest[i])
        return lca
