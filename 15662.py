# 톱니바퀴(2)
T = int(input())
T_list = []

for _ in range(T):
    T_list.append(input())

K = int(input())

def rotate(T_num,d):
    if d == 1:
        T_list[T_num] = T_list[T_num][-1] + T_list[T_num][:-1]
    elif d == -1:
        T_list[T_num] = T_list[T_num][1:] + T_list[T_num][0]


def is_linked(n1,n2): # n2 = n1+1
    if T_list[n1][2] != T_list[n2][-2]:
        return 1
    return 0


for _ in range(K):
    T_num,d = map(int,input().split(' '))
    T_num -= 1
    T_nums = [(T_num,d)]
    linked = 1
    d_c = d
    for i in range(T_num,T-1):
        d_c *= -1
        linked *= is_linked(i,i+1)
        if linked == 1:
            T_nums.append((i+1,d_c))
    linked = 1
    d_c = d
    for i in range(T_num-1,-1,-1):
        d_c *= -1
        linked *= is_linked(i,i+1)
        if linked == 1:
            T_nums.append((i,d_c))
    
    for T_num,d in T_nums:
        rotate(T_num,d)

cnt = 0
for T in T_list:
    if T[0] == '1':
        cnt += 1
print(cnt)