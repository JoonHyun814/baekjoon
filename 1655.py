# 가운데를 말해요
# import heapq

# N = int(input())
# h1 = []             #최대 힙
# h2 = []             #최소 힙
# answers = []
# answer = int(input())
# answers.append(answer)

# for _ in range(N-1):
#     num = int(input())
#     if len(h2) == 0:
#         if answer < num:
#             h2.append((num,num))
#             answers.append(answer)
#         else:
#             h2.append((answer,answer))
#             answer = num
#             answers.append(answer)
#     elif len(h1) < len(h2):
#         if num < answer:
#             answers.append(answer)
#             heapq.heappush(h1,(-num,num))
#         else:
#             if num > h2[0][1]:
#                 num2 = heapq.heappop(h2)[1]
#                 heapq.heappush(h2,(num,num))
#                 heapq.heappush(h1,(-answer,answer))
#                 answer = num2
#                 answers.append(answer)
#             else:
#                 heapq.heappush(h1,(-answer,answer))
#                 answer = num
#                 answers.append(answer)
#     else:
#         if num > answer:
#             answers.append(answer)
#             heapq.heappush(h2,(num,num))
#         else:
#             if num >= h1[0][1]:
#                 heapq.heappush(h2,(answer,answer))
#                 answer = num
#                 answers.append(answer)
#             else:
#                 num2 = heapq.heappop(h1)[1]
#                 heapq.heappush(h1,(-num,num))
#                 heapq.heappush(h2,(answer,answer))
#                 answer = num2
#                 answers.append(answer)

# for answer in answers:
#     print(answer)


import heapq

N = int(input())
h1 = []             #최대 힙
h2 = []             #최소 힙
answers = []
answer = int(input())
answers.append(answer)
h1.append((-answer,answer))

for _ in range(N-1):
    num = int(input())
    if len(h1) == len(h2):
        heapq.heappush(h1,(-num,num))
    else:
        heapq.heappush(h2,(num,num))

    if h2 and h1[0][1] > h2[0][1]:
        num1 = heapq.heappop(h1)[1]
        num2 = heapq.heappop(h2)[1]
        heapq.heappush(h2,(num1,num1))
        heapq.heappush(h1,(-num2,num2))

    answers.append(h1[0][1])    

for answer in answers:
    print(answer)