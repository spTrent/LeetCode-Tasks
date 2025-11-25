class Solution:
    def sortColors(self, array: list[int], start: int = 0, end: int | None = None) -> None:
        if end is None:
            end = len(array) - 1
        if end - start <= 0:
            return array
        i = start - 1
        pivot = array[end]
        for j in range(start, end):
            if array[j] < pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[end] = array[end], array[i + 1]
        self.sortColors(array, start, i)
        self.sortColors(array, i + 2, end)
    