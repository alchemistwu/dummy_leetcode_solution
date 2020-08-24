from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dict = {}
        for item in nums:
            if item not in count_dict.keys():
                count_dict[item] = 1
            else:
                count_dict[item] += 1

            if count_dict[item] > len(nums) // 2:
                return item