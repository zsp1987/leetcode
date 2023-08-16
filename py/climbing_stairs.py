class TopDown(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.memo = {0: 0, 1: 1, 2: 2}

        return self.helper(n)

    def helper(self, n):
        if n in self.memo:
            return self.memo[n]

        res = self.helper(n - 1) + self.helper(n - 2)
        self.memo[n] = res
        return res


class BottomUp(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        steps = [0 for i in range(n + 1)]
        steps[1] = 1
        steps[2] = 2
        for i in range(3, n + 1):
            steps[i] = steps[i - 1] + steps[i - 2]

        return steps[n]
