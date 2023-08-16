import collections


class Solution(object):
    """
    leetcode 773 https://leetcode.com/problems/flood-fill/
    """
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])

        q = collections.deque()
        visited = set()

        old_color = image[sr][sc]

        if old_color == color:
            return image

        image[sr][sc] = color
        visited.add((sr, sc))
        q.append((sr, sc))

        while q:
            cur_r, cur_c = q.popleft()
            for ri, ci in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                next_r = cur_r + ri
                next_c = cur_c + ci

                if (next_r, next_c) not in visited and next_r < m and next_r >= 0 \
                        and next_c < n and next_c >= 0 and image[next_r][next_c] == old_color:
                    image[next_r][next_c] = color
                    visited.add((next_r, next_c))
                    q.append((next_r, next_c))

        return image