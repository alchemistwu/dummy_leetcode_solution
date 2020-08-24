"""
Link:https://leetcode.com/problems/palindrome-number/
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            divided = x
            elements = []
            while(divided > 0):
                residual = divided % 10
                divided = divided // 10
                elements.append(residual)
            for i in range(len(elements) // 2 + 1):
                if elements[i] != elements[len(elements) - 1 - i]:
                    return False
        return True

if __name__ == '__main__':
    x = 12121212121
    print(Solution().isPalindrome(x))
