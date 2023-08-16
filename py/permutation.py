class Solution(object):
    """
    leetcode 46 https://leetcode.com/problems/permutations/
    """
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.result = []
        remain_set = set(nums)
        self.helper([], remain_set)
        return self.result

    def helper(self, current_list, remain_set):
        if not remain_set:
            self.result.append(current_list[:])
            return

        for num in remain_set.copy():
            current_list.append(num)
            remain_set.remove(num)
            self.helper(current_list, remain_set)
            remain_set.add(num)
            current_list.pop()