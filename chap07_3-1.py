from sys import stdin

n, m = map(int, stdin.readline().split(' '))
arr = list(map(int, stdin.readline().split(' ')))

start = 0
end = max(arr)

r = 0
while start <= end:
    sm = 0
    mid = (start + end) // 2
    for i in arr:
        if mid < i:
            sm += i - mid
    if sm < m:
        end = mid - 1
    else:
        r = mid
        start = mid + 1  
print(r)
