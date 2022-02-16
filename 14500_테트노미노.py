R,C = map(int,input().split(' '))
board = [[i for i in map(int,input().split(' '))] for _ in range(R)]

shapes = {(1,4):[[(0,0),(0,1),(0,2),(0,3)]],(4,1):[[(0,0),(1,0),(2,0),(3,0)]],(2,2):[[(0,0),(0,1),(1,0),(1,1)]],
        (3,2):[],(2,3):[]}
for i in range(3):
    shapes[(2,3)].append([(0,0),(0,1),(0,2),(1,i)])
    shapes[(2,3)].append([(1,0),(1,1),(1,2),(0,i)])
    shapes[(3,2)].append([(0,0),(1,0),(2,0),(i,1)])
    shapes[(3,2)].append([(0,1),(1,1),(2,1),(i,0)])
shapes[(3,2)].append([(0,0),(1,0),(1,1),(2,1)])
shapes[(3,2)].append([(0,1),(1,1),(1,0),(2,0)])
shapes[(2,3)].append([(0,0),(0,1),(1,1),(1,2)])
shapes[(2,3)].append([(1,0),(1,1),(0,1),(0,2)])

answer = 0
for k,v in shapes.items():
    for r in range(R-k[0]+1):
        for c in range(C-k[1]+1):
            for shape in v:
                s = 0
                for dr,dc in shape:
                    s += board[r+dr][c+dc]
                answer = max(answer,s)

print(answer)