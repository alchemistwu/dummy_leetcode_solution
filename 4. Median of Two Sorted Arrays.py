from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1 = self.qsort(nums1)
        length = len(nums1)
        index = int(length / 2)
        medium = (nums1[index] + nums1[length - index - 1]) / 2.0
        return medium

    def qsort(self, inlist):
        if inlist == []:
            return []
        else:
            pivot = inlist[0]
            lesser = self.qsort([x for x in inlist[1:] if x < pivot])
            greater = self.qsort([x for x in inlist[1:] if x >= pivot])
            return lesser + [pivot] + greater

if __name__ == '__main__':
    nums1 = []
    nums2 = [1]
    s = Solution()
    print(s.findMedianSortedArrays(nums1, nums2))