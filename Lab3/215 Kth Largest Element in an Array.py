class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_el, max_el = min(nums), max(nums)
        buckets = [0] * (max_el - min_el + 1)
        for n in nums:
            buckets[n - min_el] += 1
        i = 0
        while k > 0:
            i -= 1
            if buckets[i] and buckets[i] < k:
                k -= buckets[i]
            elif buckets[i]:
                return max_el + 1 + i
