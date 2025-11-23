from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = defaultdict(int)
        for i in s:
            chars[i] += 1
        for el in t:
            chars[el] -= 1
        return all(chars[k] == 0 for k in chars)
    