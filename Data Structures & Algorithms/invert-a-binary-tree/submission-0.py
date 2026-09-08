# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# - PROBLEM -
# Given the root of a binary tree. Invert the binary tree and return its root.
# INPUT  : [1, 2, 3, 4, 5, 6, 7]
# OUTPUT : [1, 3, 2, 7, 6, 5, 4]

# SOLUTION 01: BFS
# To invert (mirror) a binary tree, every node must swap its left and right children. We
# can process the tree level-by-level.
# (1) Start from the root.
# (2) For each node, swap each children.
# (3) Push next children into the queue.
# (4) Continue until every node has been processed
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root