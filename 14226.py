# 1.bfs(방문기록 x) 시간초과
# import queue

# S = int(input())

# mode = ['C','P','D']

# i_num = 1
# clip = 0
# time = 0
# q = queue.Queue()
# q.put((i_num,clip,time))


# while q.qsize():
#     i_num,clip,time = q.get()
#     if i_num == S:
#         print(time)
#         break
#     for m in mode:
#         if m == 'C':
#             q.put((i_num,i_num,time+1))
#         elif m == 'P':
#             q.put((i_num+clip,clip,time+1))
#         else:
#             if i_num:
#                 q.put((i_num-1,clip,time+1))

# 2. 방문기록 o
import queue

S = int(input())

mode = ['C','P','D']
i_num = 1
clip = 0
time = 0
q = queue.Queue()
q.put((i_num,clip))
visited = {(i_num,clip):time}

while q.qsize():
    i_num,clip = q.get()
    time = visited[(i_num,clip)]
    if i_num == S:
        print(time)
        break
    for m in mode:
        if m == 'C':
            if (i_num,i_num) not in visited:
                visited[(i_num,i_num)] = time+1
                q.put((i_num,i_num))
        elif m == 'P':
            if (i_num+clip,clip) not in visited:
                visited[(i_num+clip,clip)] = time+1
                q.put((i_num+clip,clip))
        else:
            if i_num and (i_num-1,clip) not in visited:
                visited[(i_num-1,clip)] = time+1
                q.put((i_num-1,clip))