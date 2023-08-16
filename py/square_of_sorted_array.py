import functools
import logging


def deprecated(func):
    @functools.wraps(func)
    def warped_func(*args, **kwargs):
        logging.warning("deprecated")
        return func(*args, **kwargs)

    return warped_func


class Solution(object):
    def sortedSquares(self, nums):
        """
        two pointer method
        :type nums: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(nums) - 1
        c = r
        res = [0] * len(nums)
        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[c] = pow(nums[l], 2)
                c -= 1
                l += 1
            else:
                res[c] = pow(nums[r], 2)
                c -= 1
                r -= 1

        return res

    @deprecated
    def sortedSquares2(self, nums):
        return sorted(x * x for x in nums)
