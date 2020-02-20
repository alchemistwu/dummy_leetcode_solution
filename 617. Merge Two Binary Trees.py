"""
Link: https://leetcode.com/problems/merge-two-binary-trees/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1

        mergedNode = TreeNode(t1.val + t2.val)

        stack = []
        tempT1 = t1
        tempT2 = t2
        tempT3 = mergedNode

        while len(stack) != 0 or tempT1 or tempT2:

            if tempT1 or tempT2:
                stack.append([tempT1, tempT2, tempT3])
                val = 0
                if tempT1:
                    if tempT1.left:
                        val += tempT1.left.val
                        tempT1 = tempT1.left
                    else:
                        tempT1 = None

                if tempT2:
                    if tempT2.left:
                        val += tempT2.left.val
                        tempT2 = tempT2.left
                    else:
                        tempT2 = None
                if tempT1 or tempT2:
                    tempT3.left = TreeNode(val)
                    tempT3 = tempT3.left
                else:
                    tempT3 = None

            else:
                val = 0
                [tempT1, tempT2, tempT3] = stack.pop(-1)
                if tempT1:
                    if tempT1.right:
                        val += tempT1.right.val
                        tempT1 = tempT1.right
                    else:
                        tempT1 = None
                if tempT2:
                    if tempT2.right:
                        val += tempT2.right.val
                        tempT2 = tempT2.right
                    else:
                        tempT2 = None

                if tempT1 or tempT2:
                    tempT3.right = TreeNode(val)
                    tempT3 = tempT3.right
                else:
                    tempT3 = None

        return mergedNode

if __name__ == '__main__':
    Node = TreeNode(3)
    Node.left = TreeNode(1)
    Node.left.left = TreeNode(1)
    Node.left.right = TreeNode(2)
    Node.right = TreeNode(4)

    Node2 = TreeNode(2)
    Node2.left = TreeNode(1)
    Node2.right = TreeNode(4)
    Node2.right.left = TreeNode(0)
    Node2.right.right = TreeNode(2)

    mergedTree = Solution().mergeTrees(Node, Node2)
    print("OK")