table_size = int(input())
table = [[0 for _ in range(table_size)] for _ in range(table_size)]

apple_num = int(input())
for i in range(apple_num):
    a = input().split(' ')
    table[int(a[0])-1][int(a[1])-1] = 2
    
moving_num = int(input())
time = 0
m = (0,1)
mode = []
for i in range(moving_num):
    condition = input().split(' ')
    mode += [m for _ in range(int(condition[0])-time)]
    time = int(condition[0])
    if condition[1] == "D":
        if m == (0,1):
            m = (1,0)
        elif m == (1,0):
            m = (0,-1)
        elif m == (0,-1):
            m = (-1,0)
        else:
            m = (0,1)
    else:
        if m == (0,1):
            m = (-1,0)
        elif m == (1,0):
            m = (0,1)
        elif m == (0,-1):
            m = (1,0)
        else:
            m = (0,-1)
mode += [m]*table_size

head = [0,0]
tail = [0,0]
table[0][0] = 1

head_time = 0
tail_time = 0

while True:
    head[0] += mode[head_time][0]
    head[1] += mode[head_time][1]

    if head[0] < 0 or head[0] >= table_size:
        print(head_time+1)
        break
    elif head[1] < 0 or head[1] >= table_size:
        print(head_time+1)
        break

    if table[head[0]][head[1]] == 1:
        print(head_time+1)
        break
    elif table[head[0]][head[1]] == 2:
        table[head[0]][head[1]] = 1
    else:
        table[tail[0]][tail[1]] = 0
        tail[0] += mode[tail_time][0]
        tail[1] += mode[tail_time][1]
        table[head[0]][head[1]] = 1
        tail_time += 1
    head_time += 1