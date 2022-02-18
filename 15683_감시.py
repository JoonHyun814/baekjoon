import sys; sys.stdin = open('15683.txt', 'r')

def dec2qua(dec_num):
    qua_num = ''
    for _ in range(len(CCTV)):
        qua_num = str(dec_num%4) + qua_num
        dec_num //= 4
    return qua_num


def sight(r,c):
    s = {1:[(r,c)],
        2:[(r,c),(-r,-c)],
        3:[(r,c),(-c,r)],
        4:[(r,c),(-r,-c),(-c,r)],
        5:[(0,1),(-1,0),(0,-1),(1,0)]}
    return s


def board_update(r,c,s):
    for dr,dc in s:
        cr,cc = r,c
        while True:
            if 0<=cr+dr<R and 0<=cc+dc<C:
                if board_c[cr+dr][cc+dc] in [0,-1]:
                    board_c[cr+dr][cc+dc] = -1
                    cr += dr
                    cc += dc
                else:
                    break
            else:
                break


def zero_cnt(board):
    cnt = 0
    for row in board:
        for cell in row:
            if cell == 0:
                cnt += 1
    return cnt

for _ in range(6):
    R,C = map(int,sys.stdin.readline().split(' '))
    board = [list(map(int,sys.stdin.readline().split(' '))) for _ in range(R)]
    head = {'0':(0,1),'1':(0,-1),'2':(1,0),'3':(-1,0)}

    CCTV = []
    for r in range(R):
        for c in range(C):
            if board[r][c] in [1,2,3,4,5]:
                CCTV.append((r,c,board[r][c]))

    answer = R*C
    for i in range(4**len(CCTV)):
        board_c = [b[:] for b in board]
        qua_num = dec2qua(i)
        for i,num in enumerate(qua_num):
            h = head[num]
            s = sight(h[0],h[1])
            r,c,num = CCTV[i]
            board_update(r,c,s[num])
        answer = min(answer,zero_cnt(board_c))

    print('pred:',answer,'answer:',sys.stdin.readline())