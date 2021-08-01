from sys import stdin
import time

start_time = time.time()

n, m = map(int, stdin.readline().split(' '))
arr = []
for _ in range(n):
    arr.append(int(stdin.readline().rstrip()))
arr.sort(reverse = True)
cnt = 0
can = 0
for i in arr:
    cnt += m // i
    m %= i
    if not m:
        can = 1
        break
if can:
    print(cnt)
else:
    print(-1)

end_time = time.time()

print(end_time - start_time)
