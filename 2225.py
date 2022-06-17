# 합분해
# 1. 문제 잘못 이해: 수가 중복되면 안된다고 읽음
# import math

# N,K = map(int,input().split(' '))
# #DP[k][n]: r을 c개의 수로 만들 수 있는 경우의 수
# DP = [[0 for _ in range(N+1)] for _ in range(K+1)] 

# # k = 1이면 항상 1
# # k = 2이면 DP[k][n] = n을 2로 나눈 수 올림
# for n in range(N+1):
#     DP[1][n] = 1
#     DP[2][n] = math.ceil(n/2)

# # DP[k][n] = DP[k-1][0] + DP[k-1][1] + ... + DP[k-1][n/2q보다 작은 정수]
# for k in range(3,K+1):
#     for n in range(N+1):
#         if k > n:
#             continue
#         i = 0
#         while i < n/2:
#             DP[k][n] += DP[k-1][i]
#             i += 1

# print(DP)
# print(DP[K][N])

# 2. 중복 가능

def solution(N,K):
    #DP[k][n]: r을 c개의 수로 만들 수 있는 경우의 수
    DP = [[0 for _ in range(N+1)] for _ in range(K+1)] 

    # k = 1이면 항상 1
    for n in range(N+1):
        DP[1][n] = 1
    if K < 2:
        return DP[K][N]%1000000000
    # DP[k][n] = DP[k-1][0] + DP[k-1][1] + ... DP[k-1][n]
    for k in range(K+1):
        for n in range(N+1):
            for i in range(n+1):
                DP[k][n] += DP[k-1][i]

    return DP[K][N]%1000000000

N,K = map(int,input().split(' '))
print(solution(N,K))