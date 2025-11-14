# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path=[]
        pathsum=[]
        if root is None:
            return False
        pathsum.append(root.val)
        path.append(root)
        while path:
            temp1=path.pop()
            temp2=pathsum.pop()
            if temp1.right is None and temp1.left is None and temp2==targetSum:
                return True
            if temp1.right:
                path.append(temp1.right)
                pathsum.append(temp1.right.val + temp2)
            
            if temp1.left:
                path.append(temp1.left)
                pathsum.append(temp1.left.val + temp2)
        return False

        