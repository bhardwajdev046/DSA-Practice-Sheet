# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sum=0
        count=0
        ans=[]
        queue=deque([root,None])
        if not root:
            return []
        while queue:
            e=queue.popleft()
            if e:
                sum+=e.val
                count+=1
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            else:
                ans.append(sum/count)
                sum,count=0,0
                if queue:
                    queue.append(None)
        return ans
        