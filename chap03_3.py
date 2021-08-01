from sys import stdin

size = int(stdin.readline().split()[0])

result = 0
for _ in range(size):
    num = map(int ,stdin.readline().split())
    min_num = min(num)
    result = max(min_num, result)
print(result)
