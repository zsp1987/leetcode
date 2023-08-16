from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix_to_words = self.build_prefixes(words)
        squares = []
        for w in words:
            self.search([w], squares, prefix_to_words)

        return squares

    def build_prefixes(self, words):
        prefix_to_words = {}

        for w in words:
            for i in range(len(w)):
                prefix = w[:i+1]
                prefix_to_words.setdefault(prefix, [])
                prefix_to_words[prefix].append(w)

        return prefix_to_words

    def search(self, square, squares, prefix_to_words):
        square_row_count = len(square[0])
        cur_row_idx = len(square)

        if square_row_count == cur_row_idx:
            squares.append(list(square))
            return

        for row_index in range(cur_row_idx, square_row_count):
            prefix = ''.join([square[i][cur_row_idx] \
                              for i in range(cur_row_idx)])
            if prefix not in prefix_to_words:
                return

        prefix = ''.join([square[i][cur_row_idx] \
                          for i in range(cur_row_idx)])

        for word in prefix_to_words.get(prefix, []):
            square.append(word)
            self.search(square, squares, prefix_to_words)
            square.pop()

sol = Solution()
print(sol.wordSquares(["baba","abab"]))