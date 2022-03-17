from itertools import combinations
import queue

board = [[0 if s == 'Y' else 1 for s in input()] for _ in range(5)]
lst = list(range(5*5))
moves = [(1,0),(-1,0),(0,1),(0,-1)]
answer = 0


def dfs(x, y):
    ret = 1
    visited[x][y] = 1

    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx = x + dx
        ny = y + dy

        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5 and board_7[nx][ny] == 1 and visited[nx][ny] == 0:
            ret += dfs(nx, ny)

    return ret


for members in combinations(lst,7):
    board_7 = [[0 for _ in range(5)] for _ in range(5)]
    cnt = 0
    for member in members:
        cnt += board[member//5][member%5]
        board_7[member//5][member%5] = 1
    if cnt < 4:
        continue

    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[members[0]//5][members[0]%5] = True

    if (dfs(members[0]//5, members[0]%5) == 7):
        answer += 1

print(answer)