"""
Link: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# Solution Recursion
class Solution_recursion:
    def __init__(self):
        self.result = []
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)
        return self.result
# Iterative solution
class Solution_iterative:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        else:
            result = []
            tree_stack = []
            temp_node = root

            while len(tree_stack) != 0 or temp_node:
                if temp_node:
                    tree_stack.append(temp_node)
                    if temp_node.left:
                        temp_node = temp_node.left
                    else:
                        temp_node = None
                else:
                    temp_pop = tree_stack.pop(-1)
                    result.append(temp_pop.val)
                    if temp_pop.right:
                        temp_node = temp_pop.right

        return result

if __name__ == '__main__':
    pass