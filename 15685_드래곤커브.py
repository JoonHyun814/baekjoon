board = [[False for _ in range(101)] for _ in range(101)]

for _ in range(int(input())):
    c,r,d,g = map(int,input().split(' '))
    direction = {0:(0,1),1:(-1,0),2:(0,-1),3:(1,0)}
    next = {(0,1):(-1,0),(-1,0):(0,-1),(0,-1):(1,0),(1,0):(0,1)}
    
    moving = [direction[d]]
    for _ in range(g):
        new_moving = []
        for m in moving[::-1]:
            new_moving.append(next[m])
        moving += new_moving

    board[r][c] = True
    for m in moving:
        r += m[0]
        c += m[1]
        board[r][c] = True

answer = 0
for r in range(100):
    for c in range(100):
        if board[r][c] and board[r+1][c] and board[r][c+1] and board[r+1][c+1]:
            answer += 1

print(answer)