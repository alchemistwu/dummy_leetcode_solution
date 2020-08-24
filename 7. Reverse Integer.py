"""
Link: https://leetcode.com/problems/reverse-integer/
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
class Solution:
    def reverse(self, x: int) -> int:
        boundry = 2 ** 31
        if x > boundry - 1 or x < - boundry:
            return 0
        if x > 0:
            divided = x
            sym = 1
        else:
            divided = - x
            sym = -1
        residual = 0
        newNum = 0
        while divided != 0:
            residual = divided % 10
            divided = divided // 10
            newNum *= 10
            newNum += residual
        newNum *= sym
        if newNum > boundry - 1 or newNum < - boundry:
            return 0
        return newNum * sym

if __name__ == '__main__':
    testcase = -12122
    print(Solution().reverse(testcase))