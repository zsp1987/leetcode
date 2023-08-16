class Solution(object):
    """
    leetcode 77 https://leetcode.com/problems/combinations/
    """
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        self.res = []

        def recurse(cur_list, cur_num):
            if len(cur_list) == k:
                self.res.append(cur_list[:])
                return

            if cur_num > n or len(cur_list) > k:
                return
            recurse(cur_list, cur_num+1)
            cur_list.append(cur_num)
            recurse(cur_list, cur_num + 1)
            cur_list.pop()

        recurse([], 1)
        return self.res
