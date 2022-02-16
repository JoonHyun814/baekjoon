import queue
import copy

r,c = map(int,input().split(' '))
board = [[i for i in map(int,input().split(' '))] for _ in range(r)]
move = [(1,0),(-1,0),(0,1),(0,-1)]
q = queue.Queue()
max_num = 0

for i in range(r):
    for j in range(c):
        visited = [[False for _ in range(c)] for _ in range(r)]
        visited[i][j] = True
        q.put((i,j,1,board[i][j],visited))
        while q.qsize():
            cr,cc,n,s,vis = q.get()
            if n == 4:
                max_num = max(max_num,s)
            else:
                for dr,dc in move:
                    v = copy.deepcopy(vis)
                    nr,nc = cr+dr, cc+dc
                    if nr >= r or nr < 0:
                        continue
                    if nc >= c or nc < 0:
                        continue
                    if vis[nr][nc]:
                        continue
                    v[nr][nc] = True
                    ns = s+board[nr][nc]
                    q.put((nr,nc,n+1,ns,v))
                    if n == 2:
                        for dr,dc in move:
                            v_c = copy.deepcopy(v)
                            nr,nc = cr+dr,cc+dc
                            if nr >= r or nr < 0:
                                continue
                            if nc >= c or nc < 0:
                                continue
                            if v[nr][nc]:
                                continue
                            v_c[nr][nc] = True
                            q.put((nr,nc,n+2,ns+board[nr][nc],v_c))
print(max_num)