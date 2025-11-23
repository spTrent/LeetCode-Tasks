class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        counter = {}
        for el in nums:
            if el in counter:
                counter[el] += 1
            else:
                counter[el] = 1
        for k in counter:
            if counter[k] == 1:
                return k
        