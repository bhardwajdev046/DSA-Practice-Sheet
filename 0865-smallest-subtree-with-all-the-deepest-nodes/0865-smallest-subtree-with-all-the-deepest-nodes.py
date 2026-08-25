# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def fun(node, depth):
            if not node:
                return None, depth

            leftLCA, left_depth = fun(node.left, depth + 1)
            rightLCA, right_depth = fun(node.right, depth + 1)

            if left_depth == right_depth:
                return node, left_depth
            if left_depth > right_depth:
                return leftLCA, left_depth
            return rightLCA, right_depth

        return fun(root, 0)[0]