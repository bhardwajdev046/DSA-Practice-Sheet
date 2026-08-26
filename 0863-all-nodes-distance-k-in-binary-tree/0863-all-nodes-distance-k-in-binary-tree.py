# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(root, parent):
            if root is None:
                return
            if root.left:
                parent[root.left] = root
                dfs(root.left, parent)
            if root.right:
                parent[root.right] = root
                dfs(root.right, parent)
    
        parent = {}
        dfs(root, parent)

        temp = []
        q = deque([(target, 0)])
        visited = {target}
        while q:
            node, dis = q.popleft()
            if dis==k:
                temp.append(node.val)
            if dis < k:
                if node.left and node.left not in visited:
                    q.append((node.left, dis+1))
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append((node.right, dis+1))
                    visited.add(node.right)
                if parent.get(node) and parent.get(node) not in visited:
                    q.append((parent[node], dis+1))
                    visited.add(parent[node])
        return temp


