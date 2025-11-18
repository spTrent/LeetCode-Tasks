class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        snums = set(nums1)
        res = []
        for el in set(nums2):
            if el in snums:
                res.append(el)
        return res
    