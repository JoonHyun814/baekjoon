# 에디터

# 방법 1. 시간초과
# in_str = list(input())
# cursor = len(in_str)

# for _ in range(int(input())):
#     order = input()
#     if order[0] == 'P':
#         in_str.insert(cursor,order.split(' ')[1])
#         cursor += 1
#         pass
#     elif order[0] == 'L':
#         if cursor == 0:
#             pass
#         else:
#             cursor -= 1
#     elif order[0] == 'D':
#         if cursor == len(in_str):
#             pass
#         else:
#             cursor += 1
#     else:
#         if cursor == 0:
#             pass
#         else:
#             cursor -= 1
#             in_str.pop(cursor)
        
# print(''.join(in_str))

str1 = list(input())
str2 = []

for _ in range(int(input())):
    order = input()
    if order[0] == 'P':
        str1.append(order.split(' ')[1])
    elif order[0] == 'L':
        if str1:
            str2.append(str1.pop())
    elif order[0] == 'D':
        if str2:
            str1.append(str2.pop())
    else:
        if str1:
            str1.pop()
        
fin_str = str1 + str2[::-1]
print(''.join(fin_str))