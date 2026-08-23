# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res=[]
        def fun(root,ans):
            if root is None:
                return []
            ans += str(root.val)
            if root.left is None and root.right is None:
                self.res.append(ans)
            else:
                ans += "->"
                fun(root.left,ans)
                fun(root.right,ans)
            # ans -= str(root.val)
            return 
        fun(root,"")
        
        return self.res
            