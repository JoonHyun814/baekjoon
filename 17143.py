R,C,M = map(int,input().split(' '))
move = {1:(-1,0),2:(1,0),3:(0,1),4:(0,-1)}

shark_map = [[False]*R for _ in range(C)]      # 포획 편의성을 위해 r,c 위치 변경
shark_list = [list(map(int,input().split(' '))) for _ in range(M)]
for shark in shark_list:
    shark[0] -= 1
    shark[1] -= 1
    if shark[3] == 1 or 2:
        shark[2] = shark[2]%(2*C-2)
    else:
        shark[2] = shark[2]%(2*R-2)
    shark[3] = move[shark[3]]
    shark_map[shark[1]][shark[0]] = shark[2:]

answer = 0

for c in range(C):      # c: 낙시왕의 위치
    # 상어 포획
    min_shark = False
    for r,shark in enumerate(shark_map[c]):
        if shark:
            shark_map[c].remove(shark)
            shark_list.remove([r,c]+shark)
            answer += shark[-1]
            break

    # 상어 위치 변경
    for shark in shark_list:
        s_r,s_c,s,d,_ = shark
        s_r += d[0]*s
        s_c += d[1]*s
        while 0 > s_r or s_r >= R or 0 > s_c or s_c >= C:
            d = (-d[0],-d[1])
            if s_r < 0:
                s_r = -s_r
            elif s_c < 0:
                s_c = -s_c
            elif s_r >= R:
                s_r = R-1+(R-1-s_r)
            elif s_c >= C:
                s_c = C-1+(C-1-s_c)
        shark[0] = s_r
        shark[1] = s_c
        shark[3] = d
    # 이동한 상어 mapping
    shark_map = [[False]*R for _ in range(C)]
    for shark in shark_list[:]:
        s_r,s_c,s,d,z = shark
        if shark_map[s_c][s_r]:
            if shark_map[s_c][s_r][2] > z:
                shark_list.remove(shark)
            else:
                shark_list.remove([s_r,s_c]+shark_map[s_c][s_r])
                shark_map[s_c][s_r] = [s,d,z]
        else:
            shark_map[s_c][s_r] = [s,d,z]
print(answer)