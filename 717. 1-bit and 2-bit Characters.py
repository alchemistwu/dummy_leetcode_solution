from typing import List
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        """
        We have two special characters. The first character can be represented by one bit 0.
        The second character can be represented by two bits (10 or 11).
        Now given a string represented by several bits.
        Return whether the last character must be a one-bit character or not.
        The given string will always end with a zero.
        :param bits:
        :return:
        """

        while len(bits) > 1:
            if bits.pop(0) == 1:
                bits.pop(0)
        if len(bits) == 1:
            return True
        return False

if __name__ == '__main__':
    bits1 = [1, 0, 0]
    print(Solution().isOneBitCharacter(bits1))