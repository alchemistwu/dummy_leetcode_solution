"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chr_list = []
        max_length = 0
        temp_length = 0
        for chr in s:
            if chr in chr_list:
                start_index = chr_list.index(chr)
                chr_list.append(chr)
                chr_list = chr_list[start_index + 1:]
                temp_length = len(chr_list)
            else:
                chr_list.append(chr)
                temp_length += 1
                if temp_length > max_length:
                    max_length = temp_length
        return max_length

if __name__ == '__main__':
    testCase = "asdasdaqwqeq"
    s = Solution()
    print("Max length: %d" % s.lengthOfLongestSubstring(testCase))