from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        l = m + n
        if (m + n) % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (self.kth(nums1, nums2, l // 2) +
                    self.kth(nums1, nums2, l // 2 - 1)) / 2

    def kth(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        mid_idx_1, mid_idx_2 = len(nums1) // 2, len(nums2) // 2
        mid_1, mid_2 = nums1[mid_idx_1], nums2[mid_idx_2]

        if mid_idx_1 + mid_idx_2 < k:
            if mid_1 > mid_2:
                return self.kth(nums1, nums2[mid_idx_2 + 1:], k - mid_idx_2 - 1)
            else:
                return self.kth(nums1[mid_idx_1 + 1:], nums2, k - mid_idx_1 - 1)
        else:
            if mid_1 > mid_2:
                return self.kth(nums1[:mid_idx_1], nums2, k)
            else:
                return self.kth(nums1, nums2[:mid_idx_2], k)
