class Solution(object):
    """
    leetcode 3 https://leetcode.com/problems/longest-substring-without-repeating-characters/
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        slow = 0
        fast = 0
        length = len(s)
        res = 0
        store_dict = set()

        while fast < length:
            cur_char = s[fast]
            if cur_char in store_dict:
                res = max(res, fast - slow)
            while cur_char in store_dict:
                slow_char = s[slow]
                store_dict.remove(slow_char)
                slow += 1
            store_dict.add(cur_char)
            fast += 1

        res = max(res, fast - slow)

        return res
