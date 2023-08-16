class Solution:

    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        i = 0
        res = ""

        def is_digit(c):
            return c in '0123456789'

        def is_char(c):
            return c in 'abcdefghijklmnopqrstuvwxyz'

        cur_str = ""
        while i < len(s):
            if is_digit(s[i]):
                num = int(s[i])
                while is_digit(s[i+1]):
                    num = num * 10 + int(s[i+1])
                    i += 1
                num_stack.append(num)
                str_stack.append(cur_str)
                cur_str = ""
                i += 1  # next mush be [

            elif is_char(s[i]):
                cur_str += s[i]
                while i+1 < len(s) and is_char(s[i+1]):
                    cur_str += s[i+1]
                    i += 1

            elif s[i] == ']':
                last_str = str_stack.pop()
                num = num_stack.pop()
                cur_str = last_str + cur_str * num

            i += 1

        for last_str in str_stack:
            res += last_str
        res += cur_str

        return res
