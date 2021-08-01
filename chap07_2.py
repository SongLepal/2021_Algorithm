from sys import stdin

def binary_search(arr, t, s, e):
    arr.sort()
    m = (s + e) // 2
    if s > e:
        return None
    if arr[m] == t:
        return m
    elif arr[m] > t:
        return binary_search(arr, t, s, m-1)
    else:
        return binary_search(arr, t, m+1, e)

n = int(stdin.readline().rstrip())
arr = list(stdin.readline().split())
m = int(stdin.readline().rstrip())
arr_ = list(stdin.readline().split())

for i in arr_:
    res = binary_search(arr, i, 0, n - 1)
    if res:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')
