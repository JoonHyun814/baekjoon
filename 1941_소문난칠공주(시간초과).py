from itertools import combinations
import queue

board = [[0 if s == 'Y' else 1 for s in input()] for _ in range(5)]
lst = list(range(5*5))
moves = [(1,0),(-1,0),(0,1),(0,-1)]
answer = 0

for members in combinations(lst,7):
    cnt = 0
    for member in members:
        cnt += board[member//5][member%5]
    if cnt < 4:
        continue

    visited = [[False for _ in range(5)] for _ in range(5)]
    q = queue.Queue()
    q.put(members[0])
    visited[members[0]//5][members[0]%5] = True

    while q.qsize():
        curr = q.get()
        for move in moves:
            next = curr + move[0]*5 + move[1]
            if curr//5 + move[0] < 0 or curr//5 + move[0] >= 5:
                continue
            if curr%5 + move[1] < 0 or curr%5 + move[1] >=5:
                continue
            if next in members and not visited[next//5][next%5]:
                q.put(next)
                visited[next//5][next%5] = True

    for member in members:
        if not visited[member//5][member%5]:
            break

    if not visited[member//5][member%5]:
        continue
    answer += 1

print(answer)