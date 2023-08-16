class Solution(object):
    """
    leetcode: 344 https://leetcode.com/problems/reverse-string/
    """
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        def swap(a, b):
            tmp = s[a]
            s[a] = s[b]
            s[b] = tmp

        l = 0
        r = len(s) - 1

        while l < r:
            swap(l, r)
            l+=1
            r-=1