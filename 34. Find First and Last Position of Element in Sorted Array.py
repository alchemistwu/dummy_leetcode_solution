from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        length = len(nums)
        start = length // 2
        pos = None

        if nums[start] > target:
            end = start
            start = 0
        elif nums[start] < target:
            end = length
        else:
            pos = start
            end = start

        while (start != end):
            new_start = (start + end) // 2
            if nums[new_start] > target:
                end = new_start
                start = 0
            elif nums[new_start] < target:
                start = new_start + 1
            else:
                pos = new_start
                break
        if pos is None:
            return [-1, -1]
        else:
            lowest = pos
            highest = pos

            while(nums[lowest - 1] == target and lowest != 0):
                lowest -= 1
            while(highest != length - 1 and nums[highest + 1] == target):
                highest += 1
            return([lowest, highest])


if __name__ == '__main__':

    print(Solution().searchRange([5, 7, 7, 7, 7, 7, 7, 8, 8, 10, 11, 11], target=7))