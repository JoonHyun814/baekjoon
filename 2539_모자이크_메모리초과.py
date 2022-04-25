def erase_board(start_point,paper_size):
    global board_c
    for i in range(paper_size):
        for j in range(paper_size):
            if start_point[0]+i<r_board and start_point[1]+j<c_board:
                board_c[start_point[0]+i][start_point[1]+j] = True


def is_possible(paper_size):
    global board_c
    board_c = [b[:] for b in board]
    cnt = 0
    for r,b_r in enumerate(board_c):
        for c,b in enumerate(b_r):
            if b == False:
                cnt += 1
                if cnt > num_papers: 
                    return False
                is_near_false = False
                for i in range(paper_size-1,0,-1):
                    check_list = []
                    for j in range(paper_size):
                        if r+j < r_board and c-i >= 0:
                            check_list.append(board_c[r+j][c-i])
                    if False in check_list:
                        erase_board((r,c-i),paper_size)
                        is_near_false = True
                        break
                
                if not is_near_false:
                    erase_board((r,c),paper_size)
    return True


c_board,r_board = map(lambda x: int(x),input().split(' '))
num_papers = int(input())
num_errors = int(input())
board = [[True for _ in range(c_board)] for _ in range(r_board)]
for _ in range(num_errors):
    c,r = map(lambda x: int(x)-1,input().split(' '))
    board[r][c] = False
paper_size = 3

while True:
    if is_possible(paper_size):
        print(paper_size)
        break