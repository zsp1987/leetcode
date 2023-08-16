from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = []
        length = len(asteroids)
        i = 0
        while i < length:
            cur = asteroids[i]
            while result and (result[-1] > 0 and cur < 0):
                if abs(result[-1]) < abs(cur):
                    result.pop()
                elif abs(result[-1]) > abs(cur):
                    cur = None
                    break
                else:
                    result.pop()
                    cur = None
                    break
            if cur:
                result.append(cur)
            i += 1
        return result
