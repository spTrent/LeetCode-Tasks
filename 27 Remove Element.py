class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        removed = 0
        for i, el in enumerate(nums[:]):
            if el == val:
                nums.pop(i - removed)
                removed += 1
        return len(nums)
