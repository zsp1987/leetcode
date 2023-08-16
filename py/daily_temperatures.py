class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for i in range(len(temperatures)):
            cur_temp = temperatures[i]
            while stack and temperatures[stack[-1]] < cur_temp:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return res
