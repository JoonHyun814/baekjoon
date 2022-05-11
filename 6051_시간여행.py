q_num = int(input())

answer_list = []
lst = []
for _ in range(q_num):
    q = input()
    if len(q)>1:
        q,v = q.split(' ')

        # a 처리
        if q == 'a':
            lst.append(v)

        # t 처리
        else:
            if int(v) == 1: #########tq
                lst = []
            else:
                lst = answer_list[int(v)-2][:]

    # s 처리
    else:
        if lst == []:
            pass
        else:
            lst.pop()

    answer_list.append(lst[:])

for lst in answer_list:
    print(lst[-1] if lst != [] else -1)