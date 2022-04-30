#### 종이는 바닥에 딱 맞게 붙여야 한다!
def erase(r,c,paper_size,error_list_c):
    lst = []
    for idx in range(len(error_list_c)):
        e_r,e_c = error_list_c[idx]
        if e_r >= r + paper_size:
            break
        if e_c >= c and e_c <= c_board and e_c < c + paper_size:
            lst.append(idx)

    for i,idx in enumerate(lst):
        error_list_c.pop(idx-i)


def is_possible(paper_size):
    error_list_c = error_list[:]
    
    for _ in range(num_papers):
        if error_list_c == []:
            return True
        print(error_list_c)
        error = error_list_c.pop(0)
        
        start_c = error[1]
        for near_error in error_list_c:
            if near_error[0] >= error[0] + paper_size:
                break
            if near_error[1] <= error[1] - paper_size:
                pass
            elif near_error[1] >= error[1]:
                pass
            else:
                start_c = min(start_c,near_error[1])
        erase(error[0],start_c,paper_size,error_list_c)
        print(error[0],start_c)
    print(error_list_c)
    if error_list_c == []:
        return True
    else:
        return False


c_board,r_board = map(lambda x: int(x),input().split(' '))
num_papers = int(input())
num_errors = int(input())
error_list = []
for _ in range(num_errors):
    c,r = map(lambda x: int(x),input().split(' '))
    error_list.append((r,c))
error_list.sort()

paper_size = 0
while True:
    paper_size += 1
    if is_possible(paper_size):
        print(paper_size)
        break