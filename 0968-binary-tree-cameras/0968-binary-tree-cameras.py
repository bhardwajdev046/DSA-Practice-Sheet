# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def fun(self,root):
        if root is None:
            return 1
        left_n = self.fun(root.left)
        right_n = self.fun(root.right)

        if (left_n==-1 or right_n==-1):
            self.camera+=1
            return 0
        if (left_n==0 or right_n==0):
            return 1
        return -1

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera=0
        if self.fun(root)==-1:
            self.camera+=1
        return self.camera