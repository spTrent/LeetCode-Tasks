from collections import defaultdict

class Solution:
    def sort(self, array: list, start: int = 0, end: int | None = None) -> None:
        if end is None:
            end = len(array) - 1
        if end - start <= 0:
            return array
        i = start - 1
        pivot = array[end]
        for j in range(start, end):
            if array[j][1] > pivot[1]:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i+1], array[end] = array[end], array[i+1]
        self.sort(array, start, i)
        self.sort(array, i + 2, end)
        return array
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        counter = [(n, count) for n, count in counter.items()]
        counter = self.sort(counter)
        return [n for n, count in counter[:k]]
    