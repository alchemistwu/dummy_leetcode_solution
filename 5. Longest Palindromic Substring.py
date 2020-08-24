"""
Link: https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length == 0:
            return ""
        max_indice = (0, 0)
        palindrome = dict()
        for i in range(length - 1, -1, -1):
            for j in range(i, length):
                if i == j:
                    palindrome[(i, j)] = True
                elif i == j - 1:
                    palindrome[(i, j)] = s[i] == s[j]
                else:
                    palindrome[(i, j)] = (s[i] == s[j] and palindrome[(i + 1, j - 1)])
                if palindrome[(i, j)] and (j - i + 1) > (max_indice[1] - max_indice[0] + 1):
                    max_indice = (i, j)
        return s[max_indice[0]: max_indice[1] + 1]
if __name__ == '__main__':
    # testcase = "jklaecabaceefg"
    testcase = "bb"
    print(Solution().longestPalindrome(testcase))