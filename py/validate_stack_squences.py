from collections import deque
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        count = len(popped)
        push_stack = deque(pushed)
        temp_stack = deque()
        i = 0
        while i < count:
            cur = popped[i]
            if temp_stack and temp_stack[-1] == cur:
                temp_stack.pop()
                i += 1
                continue
            while push_stack and push_stack[0] != cur:
                temp_stack.append(push_stack.popleft())
            if not push_stack:
                return False
            else:
                push_stack.popleft()
                i += 1
        return True
    
Solution().validateStackSequences([1,2,3,4,5], [4,5,3,2,1])