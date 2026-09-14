# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Iterative DFS, simulate the recursive call stack using an explicit stack
# Inorder Traversal: Left Subtree -> Current Node > Right Subtree

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, curr = [], root

        res = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                res.append(curr.val)
                curr = curr.right
        return res
        