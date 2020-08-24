# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            length = len(nums)
            mid_start = length // 2

            root = TreeNode(nums[mid_start])
            root.left = self.sortedArrayToBST(nums[:mid_start])
            root.right = self.sortedArrayToBST(nums[mid_start + 1: length])
            return root

        return
