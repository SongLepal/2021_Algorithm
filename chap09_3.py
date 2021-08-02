from sys import stdin
import heapq as hq
INF = 999

'''
n: 도시의 개수
m: 통로의 개수
c: 수신 희망 도시
'''

def dijkstra(start):
    que = []
    hq.heappush(que, (0, start))
    distance[start] = 0
    while que:
        dist, now = hq.heappop(que)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hq.heappush(que, (cost, i[0]))

arr = list(map(int, stdin.readline().split(' ')))
n, m, c = arr[0], arr[1], arr[2] - 1

graph = [[] for _ in range(n)]
distance = [INF] * n

for _ in range(m):
    arr = list(map(int, stdin.readline().split(' ')))
    x, y, z = arr[0] - 1, arr[1] - 1, arr[2]
    graph[x].append((y, z))

dijkstra(c)

cnt = 0
max_dist = 0
for i in distance:
    if i != INF:
        cnt += 1
        max_dist = max(max_dist, i)
print(cnt - 1, max_dist)
