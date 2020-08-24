class Solution:
    def titleToNumber(self, s: str) -> int:
        length = len(s)
        result = 0
        for i in range(length):
            result += (ord(s[i]) - ord('A') + 1) * (26 ** (length - i - 1))
        return result