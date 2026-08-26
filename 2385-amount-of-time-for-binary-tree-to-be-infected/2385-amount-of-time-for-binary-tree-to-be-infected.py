# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # har node ka parent store krne k liye
        def parentNodes(root, parent):
            if root is None:
                return
            if root.left:
                parent[root.left]=root
                parentNodes(root.left,parent)
            if root.right:
                parent[root.right]=root
                parentNodes(root.right,parent)
        parent={}
        parentNodes(root, parent)

       # start int m h toh usko as a root use krna h, isiliye 
        def findNode(root, k):
            if root is None:
                return None
            if root.val == k:
                return root
            left = findNode(root.left, k)
            if left:
                return left
            return findNode(root.right, k)
        target = findNode(root, start)

        k=0
        q = deque([(target, 0)])
        visited = {target}
        while q:
            node, dis = q.popleft()
            k = max(k,dis)
            if node.left and node.left not in visited:
                q.append((node.left, dis+1))
                visited.add(node.left)
            if node.right and node.right not in visited:
                q.append((node.right, dis+1))
                visited.add(node.right)
            if parent.get(node) and parent.get(node) not in visited:
                q.append((parent[node], dis+1))
                visited.add(parent[node])
            
        return k
