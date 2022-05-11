n = int(input())
wine_list = [int(input()) for _ in range(n)]

def solution(n,wine_list):
    if n <= 2:
        return sum(wine_list)
    dp = [wine_list[0],wine_list[1]+wine_list[0],0]
    dp[2] = max(dp[1],dp[0]+wine_list[2],wine_list[1]+wine_list[2])

    for i in range(3,n):
        dp.append(max(dp[i-1],dp[i-2]+wine_list[i],dp[i-3]+wine_list[i]+wine_list[i-1]))
    return dp[-1]

print(solution(n,wine_list))