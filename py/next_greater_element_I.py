class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []
        if len(nums1) == 1:
            return [-1]

        next_map = {}
        stack = []
        stack.append(nums2[0])
        next_map[nums2[0]] = -1
        for i in range(1,len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                next_map[stack[-1]] = cur
                stack.pop()
            stack.append(cur)
            next_map[cur] = -1

        print(next_map)

        res = []
        for i in range(len(nums1)):
            if nums1[i] in next_map:
                res.append(next_map[nums1[i]])
            else:
                res.append(-1)
        return res