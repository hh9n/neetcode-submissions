# 二元樹的直徑（diameter）被定義為樹中任意兩節點間最長路徑的長
# 度，此一路徑不需要經過 root 節點。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# -- Brute Force --
# The longest Path of a node = height of left subtree + height of right subtree
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.maxHeight(root.left)
        right_height = self.maxHeight(root.right)
        diameter = left_height + right_height

        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))
        