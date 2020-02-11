from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution_list = []
        nums.sort()
        length = len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            head = i + 1
            tail = length - 1
            while(head < tail):
                temp_list = [nums[i], nums[tail], nums[head]]
                temp_sum = sum(temp_list)

                if temp_sum == 0:
                    solution_list.append(temp_list)
                    while head < tail and nums[head + 1] == nums[head]:
                        head += 1
                    while head < tail and nums[tail - 1] == nums[tail]:
                        tail -= 1
                    tail -= 1
                    head += 1
                elif temp_sum > 0:
                    tail -= 1
                else:
                    head += 1
        return solution_list

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    S = Solution()
    print(S.threeSum(nums))
