# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def traverse(node, depth):
            if node:
                depth = max(traverse(node.left, depth + 1), traverse(node.right, depth + 1))
            return depth

        return traverse(root, 0)

