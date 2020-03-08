"""
Link: https://leetcode.com/problems/valid-parentheses/
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        stack = []
        for i in range(len(s)):
            if len(stack) > 0:
                if (stack[-1] == "(" and s[i] == ")") or (stack[-1] == "[" and s[i] == "]") or (stack[-1] == "{" and s[i] == "}"):
                    stack.pop(-1)
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        if len(stack) == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "()[]{}"
    print(Solution().isValid(s))