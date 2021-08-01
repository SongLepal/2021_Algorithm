from sys import stdin

_input = stdin.readline()
row = int(_input[1])-1
col = int(ord(_input[0])-ord('a'))

moves = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]
cnt = 0

for move in moves:
    n_row = row + move[0]
    n_col = col + move[1]
    if n_row >= 0 and n_row <= 7 and n_col >= 0 and n_col <= 7:
        cnt += 1
print(cnt)
