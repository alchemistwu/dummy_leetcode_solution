"""
Link: https://leetcode.com/problems/validate-binary-search-tree/
"""
from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = []
        temp_node = root
        val = - float('inf')

        while len(stack) != 0 or temp_node:
            if temp_node:
                stack.append(temp_node)
                if temp_node.left:
                    temp_node = temp_node.left
                else:
                    temp_node = None
            else:
                temp_pop = stack.pop(-1)
                if temp_pop.val > val:
                    val = temp_pop.val
                else:
                    return False
                if temp_pop.right:
                    temp_node = temp_pop.right

        return True
