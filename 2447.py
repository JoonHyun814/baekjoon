# 별찍기
N = int(input())

def f(n,i):
    if n == 3:
        if i == 0:
            print('*'*3,end='')
        elif i == 1:
            print('* *',end='')
        elif i == 2:
            print('*'*3,end='')
    else:
        if i//(n//3) == 1:
            f(n//3,i%(n//3))
            print(' '*(n//3),end='')
            f(n//3,i%(n//3))
        else:
            f(n//3,i%(n//3))
            f(n//3,i%(n//3))
            f(n//3,i%(n//3))


for i in range(N):
    f(N,i)
    if i == N-1:
        pass
    else:
        print('')