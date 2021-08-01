from sys import stdin

n = int(stdin.readline().strip())

def setting(arr):
    return arr[1]

arr = []
for _ in range(n):
    _input = stdin.readline().split()
    arr.append((_input[0], int(_input[1])))
    
arr.sort(key = setting)
for i in range(n):
    print(arr[i][0], end = " ")
