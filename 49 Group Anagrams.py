from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        sorted_str = defaultdict(list)
        for s in strs:
            sorted_str[tuple(sorted(s))].append(s)
        return [v for v in sorted_str.values()]
    

"""
Решение выше быстрее, но это мне нравится больше, потому что сложность О(nk) меньше, чем О(nk * logk):
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        letters_str = defaultdict(list)
        for s in strs:
            letters = [0] * 26
            for el in s:
                letters[ord(el)-97] += 1
            letters_str[tuple(letters)].append(s)
        return [v for v in letters_str.values()]
"""
