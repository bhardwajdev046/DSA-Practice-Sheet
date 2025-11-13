# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        
        # If the node to delete is the root
        if root.val == key:
            return self.deletion(root)
        
        temp = root
        while temp:
            if key < temp.val:
                if temp.left and temp.left.val == key:
                    temp.left = self.deletion(temp.left)
                    break
                else:
                    temp = temp.left
            else:
                if temp.right and temp.right.val == key:
                    temp.right = self.deletion(temp.right)
                    break
                else:
                    temp = temp.right
                    
        return root

    def deletion(self, node: TreeNode) -> Optional[TreeNode]:
        # Case 1: No left child
        if node.left is None:
            return node.right
        # Case 2: No right child
        elif node.right is None:
            return node.left
        # Case 3: Two children
        else:
            right_child = node.right
            last_right = self.findLastRight(node.left)
            last_right.right = right_child
            return node.left

    def findLastRight(self, node: TreeNode) -> TreeNode:
        while node.right:
            node = node.right
        return node
