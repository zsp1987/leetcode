class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = []
        self.generate("", n, n)
        return self.result

    def generate(self, cur, left, right):
        if right < left or left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            self.result.append(cur)
        self.generate(cur + "(", left-1, right)
        self.generate(cur + ")", left, right-1)
