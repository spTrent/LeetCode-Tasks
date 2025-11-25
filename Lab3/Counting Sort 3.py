n = int(input())
arr = []
for _ in range(n):
    digit, string = input().split()
    arr.append(int(digit))
    
counter = [0] * 100
for n in arr:
    counter[n] += 1
prefix_sum = 0
for i in range(100):
    prefix_sum += counter[i]
    print(prefix_sum, end=' ')
