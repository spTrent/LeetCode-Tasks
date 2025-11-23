class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count1 = {}
        res = []
        for n in nums1:
            if n in count1:
                count1[n] += 1
            else:
                count1[n] = 1
        for n in nums2:
            if n in count1 and count1[n] > 0:
                res.append(n)
                count1[n] -= 1
        return res
    