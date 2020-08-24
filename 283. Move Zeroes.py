from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = []
        for i in range(len(nums)):
            if nums[i] != 0:
                new_nums.append(nums[i])
        for i in range(len(nums)):
            if i < len(new_nums):
                nums[i] = new_nums[i]
            else:
                nums[i] = 0
        # solution 1:
#         for i in range(len(nums)):
#             if nums[i] != 0:
#                 continue

#             j = i + 1
#             while(j < len(nums)):
#                 if nums[j] != 0:
#                     break
#                 j += 1

#             if j == len(nums):
#                 break
#             else:
#                 nums[i], nums[j] = nums[j], nums[i]

