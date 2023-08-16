from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ps = [(p[0], p[1], pow(p[0], 2) + pow(p[1], 2)) for p in points]
        def quick_sort(points, start, end, k):
            if end - start < 1:
                return
            piv = start
            for i in range(start, end):
                cur_v = points[i][2]
                if cur_v <= points[end][2]:
                    swap(points, i, piv)
                    piv += 1
            swap(points, end, piv)
            quick_sort(points, start, piv-1)
            if piv + 1 < k:
                quick_sort(points, piv + 1, end)

        def swap(points, a, b):
            temp = points[a]
            points[a] = points[b]
            points[b] = temp

        quick_sort(ps, 0, len(ps) - 1)

        return [[k[0], k[1]] for k in ps[0:k]]
                

sol = Solution()
sol.kClosest([[1,3],[-2,2]], 1)