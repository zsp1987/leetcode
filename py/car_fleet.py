class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        pairs = list(zip(position, speed))
        pairs.sort()
        stack = []
        for i in range(len(pairs)):
            cur_pair = pairs[i]
            while stack and stack[-1][1] > cur_pair[1]:
                if cur_pair[0] + (cur_pair[0] - stack[-1][0]) / float(stack[-1][1] - cur_pair[1]) * cur_pair[1] <= target:
                    stack.pop()
                else:
                    break

            stack.append(cur_pair)
        return len(stack)
