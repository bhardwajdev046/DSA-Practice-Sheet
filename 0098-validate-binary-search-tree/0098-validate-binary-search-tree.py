# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self,temp,l,r):
        if temp is None:
            return True
        if not l<temp.val<r:
            return False
        left=self.solve(temp.left,l,temp.val)
        if left==False:
            return False
        right=self.solve(temp.right,temp.val,r)
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l=float('-inf')
        r=float('inf')
        return self.solve(root,l,r)
        # li=[]
        # def inorder(root):
        #     if root is None:
        #         return
        #     inorder(root.left)
        #     li.append(root.val)
        #     inorder(root.right)

        # inorder(root)
        # for i in range(1,len(li)):
        #     if li[i] <= li[i-1]:
        #         return False
        # return True
        