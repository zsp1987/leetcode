class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        for i in range(len(num)):
            cur = int(num[i])
            while stack and stack[-1] > cur:
                if k == 0:
                    break
                stack.pop()
                k -= 1
            stack.append(cur)
        while k > 0:
            stack.pop()
            k -= 1

        if not stack:
            return "0"

        res = ""
        i = 0
        if stack[0] == 0:
            while i < len(stack) and stack[i] == 0:
                i += 1

        if i == len(stack):
            return "0"

        while i < len(stack):
            res += str(stack[i])
            i += 1

        return res
