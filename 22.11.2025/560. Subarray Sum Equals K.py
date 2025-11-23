from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        sums = defaultdict(int)
        sums[0] = 1
        count = 0
        prefix_sum = 0
        for el in nums:
            prefix_sum += el
            count += sums[prefix_sum - k]
            sums[prefix_sum] += 1
        return count
