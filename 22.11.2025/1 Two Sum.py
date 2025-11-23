class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        snums = set(nums)
        for i, num in enumerate(nums):
            if (target - num) in snums:
                j = nums.index(target - num)
                if i != j and j != -1:
                    return [i, j]
