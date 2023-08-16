class Solution(object):
    """
    :leetcode 784 
    :url https://leetcode.com/problems/letter-case-permutation/
    """
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.output = []
        self.helper(s, "", 0)

        return self.output

    def helper(self, s, cur_str, cur_idx):
        if len(cur_str) == len(s):
            self.output.append(cur_str[:])
            return

        cur_char = s[cur_idx]
        if cur_char.isalpha():
            self.helper(s, cur_str + cur_char.lower(), cur_idx + 1)
            self.helper(s, cur_str + cur_char.upper(), cur_idx + 1)
        else:
            self.helper(s, cur_str + cur_char, cur_idx + 1)
