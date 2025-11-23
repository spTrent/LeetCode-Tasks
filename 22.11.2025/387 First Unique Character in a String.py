from collections import defaultdict


class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = defaultdict(int)
        for i, el in enumerate(s):
            if el in chars:
                chars[el] = -1
            else:
                chars[el] = i
        for k, v in chars.items():
            if v >= 0:
                return v
        return -1