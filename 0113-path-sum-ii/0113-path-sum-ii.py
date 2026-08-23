# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans=[]

        def fun(root, targetSum, res):
            if root is None:
                return
            
            res.append(root.val)
            if not root.left and not root.right:
                if targetSum==root.val:
                    self.ans.append(res.copy())
            else: 
                #left explore
                fun(root.left, targetSum-root.val, res)    
                #right explore 
                fun(root.right, targetSum-root.val, res)

            # BACKTRACK
            res.pop()
        fun(root, targetSum, [])
        return self.ans