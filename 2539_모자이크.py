def is_possible(error_list,paper_size):
    cnt = 0
    while True:
        cnt += 1
        if cnt > num_papers:
            return False
        error = error_list.pop()
        for e in error_list[::-1]:
            if error[0]-paper_size < e[0] <= error[0]:
                error_list.pop()
            else:
                break
        if error_list == []:
            return True


c_board,r_board = map(lambda x: int(x),input().split(' '))
num_papers = int(input())
num_errors = int(input())
error_list = []
max_c = 0
for _ in range(num_errors):
    c,r = map(lambda x: int(x),input().split(' '))
    error_list.append((r,c))
    max_c = max(max_c,c)
error_list.sort()
paper_size = max_c

while True:
    if is_possible(error_list[:],paper_size):
        print(paper_size)
        break
    else:
        paper_size += 1