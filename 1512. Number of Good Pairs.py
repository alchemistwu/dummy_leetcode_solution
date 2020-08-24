from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        while (len(nums) > 0):
            tmp_count = 0
            cur = nums[0]
            for i in range(1, len(nums)):
                if nums[i] == cur:
                    tmp_count += 1
            count += int((tmp_count + 1) * tmp_count / 2)
            for _ in range(0, tmp_count + 1):
                nums.remove(cur)
        return count


if __name__ == '__main__':
    print(Solution().numIdenticalPairs([2,2,1,4,1,5,1,2]))