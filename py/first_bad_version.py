def isBadVersion():
    return True

class Solution(object):
    """
    :leetcode: 278
    :url: https://leetcode.com/problems/first-bad-version/
    """
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n - 1
        while left < right:
            mid = left + (right - left) / 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left if isBadVersion(left) else left + 1