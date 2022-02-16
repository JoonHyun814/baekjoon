r_num,c_num,r,c,comd_num = map(int,input().split(' '))

table = [[] for _ in range(r_num)]
for t in table:
    for num in map(int,input().split(' ')):
        t.append(num)

commands = input().split(' ')
dice = {1:0,2:0,3:0,4:0,5:0,6:0}
rolling = {'1':(1,4,6,3),'2':(1,3,6,4),'3':(1,5,6,2),'4':(1,2,6,5)}
moving = {'1':(0,1),'2':(0,-1),'3':(-1,0),'4':(1,0)} 
for comd in commands:
    if r + moving[comd][0] < 0 or r + moving[comd][0] >= r_num:
        continue
    if c + moving[comd][1] < 0 or c + moving[comd][1] >= c_num:
        continue
    r += moving[comd][0]
    c += moving[comd][1]
    
    dice1 = dice[rolling[comd][0]]
    for i in range(1,4):
        dice[rolling[comd][i-1]] = dice[rolling[comd][i]]
    dice[rolling[comd][3]] = dice1
    
    if table[r][c] == 0:
        table[r][c] = dice[6]
    else:
        dice[6] = table[r][c]
        table[r][c] = 0
    print(dice[1])