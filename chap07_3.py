from sys import stdin

n, m = map(int, stdin.readline().split(' '))
arr = list(map(int, stdin.readline().split(' ')))

h = max(arr)
s = 0
while True:
    if s >= m:
        print(h)
        break
    for i in arr:
        if h < i:
            s += i - h
    h -= 1
