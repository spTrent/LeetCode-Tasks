class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        l = len(s)
        res = 0
        for el in s:
            curr = 1
            if el - 1 not in s:
                for i in range(1, l):
                    if el + i in s:
                        curr += 1
                    else:
                        break
                res = max(res, curr)
        return res
