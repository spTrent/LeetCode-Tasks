from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        counter = [(n, count) for n, count in counter.items()]
        counter.sort(key=lambda x: -x[1])
        return [n for n, count in counter[:k]]
