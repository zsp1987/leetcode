"""
:leetcode 84
:url https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

from collections import deque


class Solution(object):

    def largestRectangleArea(self, heights):

        max_area = 0
        length = len(heights)
        mono_stack = deque()

        for right_boundary in range(length + 1):
            right_boundary_height = -1 if right_boundary == length \
                else heights[right_boundary]
            while mono_stack and heights[mono_stack[-1]] > right_boundary_height:
                curr_height = heights[mono_stack.pop()]
                left_boundary = mono_stack[-1] if mono_stack else -1
                curr_width = right_boundary - left_boundary - 1
                max_area = max(max_area, curr_width * curr_height)

            mono_stack.append(right_boundary)

        return max_area
