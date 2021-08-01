from sys import stdin

n, k = map(int, stdin.readline().split())

arrA = list(map(int, stdin.readline().split()))
arrB = list(map(int, stdin.readline().split()))

arrA.sort()
arrB.sort(reverse = True)
for i in range(k):
    arrA[i] = arrB[i]
print(sum(arrA))
