# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def leftheight(root):
            count=0
            while root:
                count+=1
                root=root.left
            return count
        
        def rightheight(root):
            count=0
            while root:
                count+=1
                root=root.right
            return count

        lh = leftheight(root)
        rh = rightheight(root)
        if lh ==rh:
            return (2**lh)-1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)