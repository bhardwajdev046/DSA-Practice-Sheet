# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if root is None:
            return []
        queue.append(root)
        flag=1
        ans=[]
        while queue:
            level = []
            for i in range(len(queue)):
                e = queue.popleft()
                level.append(e.val)
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            if flag%2 == 0:
                level = level[::-1]
            ans.append(level)
            flag+=1
        return ans