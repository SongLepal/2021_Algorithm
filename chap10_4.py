from sys import stdin
from collections import deque
import copy

def topology_sort():
    res = copy.deepcopy(time)
    que = deque()

    for i in range(n):
        if indegree[i] == 0:
            que.append(i)
            
    while que:
        now = que.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            res[i] = max(res[i], res[now] + time[i])

            if indegree[i] == 0:
                que.append(i)
    for i in range(n):
        print(res[i])

n = int(stdin.readline().rstrip())

indegree = [0 for i in range(n)]
graph = [[] for i in range(n)]
time = []

for i in range(n):
    arr = list(map(int, stdin.readline().split()))
    time.append(arr[0])
    for j in arr[1:-1]:
        indegree[i] += 1
        graph[j-1].append(i)

topology_sort()
