# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # self.result=0
        # def traversal(root):
        #     if  root is None:
        #         return 
        #     if root.val>=low:                                    #my approach
        #         traversal(root.left)
        #     if root.val<=high:
        #         traversal(root.right)
        #     if root.val>=low and root.val<=high:
        #         self.result+=root.val
            
        # traversal(root)
        # return self.result
        
        result=0
        if root is None:
            return 0
        if root.val>=low:
            result+=self.rangeSumBST(root.left,low,high)
        if root.val<=high:
            result+=self.rangeSumBST(root.right,low,high)
        if root.val>=low and root.val<=high:
            result+=root.val
        return result