from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result_dict = {}

        class Item:
            def __init__(self, val=length - 1, flag=False):
                self.val = val
                self.flag = flag

        for i in range(length):
            result_dict[nums[i]] = Item()

        for i in range(length):
            if result_dict[nums[i]].flag:
                break

            for j in range(i + 1, length):
                if nums[i] >= nums[j]:
                    result_dict[nums[j]].val = result_dict[nums[j]].val - 1
                if nums[i] <= nums[j]:
                    result_dict[nums[i]].val = result_dict[nums[i]].val - 1

            result_dict[nums[i]].flag = True

        result_list = []

        for i in range(length):
            result_list.append(result_dict[nums[i]].val)

        return result_list

if __name__ == '__main__':
    print(Solution().smallerNumbersThanCurrent([8,1,2,2,3]))