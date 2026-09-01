# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q=deque([(root, 0, 0)])
        hash = {}
        while q:
            for i in range(len(q)):
                temp = q.popleft()
                node = temp[0]
                depth = temp[1]
                h_dis = temp[2]
                if h_dis not in hash:
                    hash[h_dis]=[]
                hash[h_dis].append((node.val, depth))
                if node.left:
                    q.append((node.left, depth+1, h_dis-1))
                if node.right:
                    q.append((node.right, depth+1, h_dis+1))
        for h_dis in hash:
            hash[h_dis].sort(key=lambda x: (x[1], x[0]))
        ans=[]
        for h_d,node in sorted(hash.items()):
            arr=[]
            for x in node:
                arr.append(x[0])
            ans.append(arr)
        return ans