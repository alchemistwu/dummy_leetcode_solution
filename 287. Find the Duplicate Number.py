"""
https://leetcode.com/problems/find-the-duplicate-number/
"""
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        quick = 0
        slow = 0
        while True:
            quick = nums[nums[quick]]
            slow = nums[slow]
            if quick == slow:
                break
        pt1 = 0
        pt2 = slow
        while(pt1 != pt2):
            pt1 = nums[pt1]
            pt2 = nums[pt2]
        return pt1

if __name__ == '__main__':
    nums = [4, 2, 3, 4, 1]
    print(Solution().findDuplicate(nums))
