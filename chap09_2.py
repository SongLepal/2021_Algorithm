from sys import stdin
INF = 999

'''
n: 회사의 개수
m: 경로의 개수
x: 판매 회사
k: 소개팅 위치
'''

n, m = map(int, stdin.readline().split(' '))
graph = [[INF] * (n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0

for _ in range(m):
    arr = list(map(int, stdin.readline().split(' ')))
    i, j = arr[0] - 1, arr[1] - 1
    graph[i][j], graph[j][i] = 1, 1

arr = list(map(int, stdin.readline().split(' ')))
x, k = arr[0] - 1, arr[1] - 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[k][j] + graph[i][k])

if graph[0][k] + graph[k][x] <= INF:
    print(graph[0][k] + graph[k][x])
else:
    print(-1)

