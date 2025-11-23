class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1:
            s = sum(map(lambda x: int(x)**2, str(n)))
            if s in visited:
                return False
            n = s
            visited.add(s)
        else:
            return True
