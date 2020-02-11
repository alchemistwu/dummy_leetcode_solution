from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        max = 0
        left_index = 0
        right_index = length - 1
        while right_index != left_index:
            area = min(height[right_index], height[left_index]) * (right_index - left_index)
            if area > max: max = area
            if height[left_index] < height[right_index]:
                pos = left_index + 1
                while(height[pos] < height[left_index] and height[pos] < height[right_index] and pos != right_index):
                    pos += 1
                left_index = pos
            else:
                pos = right_index - 1
                while (height[pos] < height[left_index] and height[pos] < height[right_index] and pos != left_index):
                    pos -= 1
                right_index = pos
        return max



if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([2,3,4,5,18,17,6]))