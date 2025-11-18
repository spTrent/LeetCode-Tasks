class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = len(set(nums))
        nums[:l] = sorted(set(nums))
        return l
    