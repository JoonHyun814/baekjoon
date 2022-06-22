# 오큰수
N = int(input())
nums = list(map(int,input().split(' ')))
out = [-1]*N

stack = [0]
for i in range(1,N):
    while stack and nums[stack[-1]] < nums[i]:
        j = stack.pop()
        out[j] = nums[i]
    stack.append(i)

print(" ".join(map(str,out)))