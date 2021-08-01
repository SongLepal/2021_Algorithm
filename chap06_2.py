from sys import stdin

n = int(stdin.readline().strip())

arr = []
for _ in range(n):
    arr.append(int(stdin.readline().strip()))

arr.sort(reverse = True)

for i in range(n):
    print(arr[i], end = " ")
