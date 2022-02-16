N,M,K = map(int,input().split(' '))
A = [[i for i in map(int,input().split(' '))] for _ in range(N)]
board = [[5 for _ in range(N)] for _ in range(N)]

trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r,c,age = map(int,input().split(' '))
    trees[r-1][c-1].append(age)
for r in range(N):
    for c in range(N):
        trees[r][c].sort()

near = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

for _ in range(K):
    ######## 봄,여름
    for r in range(N):
        for c in range(N):
            for n,age in enumerate(trees[r][c]):
                if board[r][c] >= age:
                    board[r][c] -= age
                    trees[r][c][n] += 1
                else:
                    for _ in range(len(trees[r][c])-n):
                        board[r][c] += trees[r][c].pop()//2
                    break

    ######## 가을,겨울
    for r in range(N):
        for c in range(N):
            board[r][c] += A[r][c]
            for age in trees[r][c]:
                if age%5 == 0:
                    for dr,dc in near:
                        if r+dr < 0 or r+dr >= N: continue
                        if c+dc < 0 or c+dc >= N: continue
                        trees[r+dr][c+dc].insert(0,1)

answer = 0
for tree_row in trees:
    for tree in tree_row:
        answer += len(tree)
print(answer)