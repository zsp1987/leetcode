class Solution(object):
    """
    leetcode 567 https://leetcode.com/problems/permutation-in-string/
    """
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        slow = 0
        fast = 0
        s1_length = len(s1)
        s2_length = len(s2)
        counter = [0] * 26
        cur_length = 0

        for i in range(s1_length):
            cur_char = ord(s1[i]) - ord('a')
            counter[cur_char] = counter[cur_char] + 1

        cur_counter = [0] * 26
        while fast < s2_length:
            fast_char = ord(s2[fast]) - ord('a')
            fast += 1
            if counter[fast_char]:
                if cur_counter[fast_char] == counter[fast_char]:
                    while ord(s2[slow]) - ord('a') != fast_char:
                        slow_char = ord(s2[slow]) - ord('a')
                        cur_counter[slow_char] = cur_counter[slow_char] - 1
                        cur_length -= 1
                        slow += 1
                    slow_char = ord(s2[slow]) - ord('a')
                    cur_counter[slow_char] = cur_counter[slow_char] - 1
                    cur_length -= 1
                    slow += 1
                cur_counter[fast_char] = cur_counter[fast_char] + 1
                cur_length += 1
                if cur_length == s1_length:
                    return True
            else:
                cur_counter = [0] * 26
                cur_length = 0
                slow = fast

        return False
