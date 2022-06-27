#우수마을
# 1. dfs (메모리 초과)
# N = int(input())
# populations = [0]+list(map(int,input().split(' ')))
# max_pop = 0
# visited = [True]+[False]*N
# path_dict = {}
# for _ in range(N-1):
#     town1,town2 = map(int,input().split(' '))
#     if town1 in path_dict:
#         path_dict[town1].append(town2)
#     else:
#         path_dict[town1] = [town2]
#     if town2 in path_dict:
#         path_dict[town2].append(town1)
#     else:
#         path_dict[town2] = [town1]


# def dfs(i,pop):
#     # print(i,visited,pop)
#     global max_pop,visited
#     visited[i] = True
#     added_visits = [i]
#     for path in path_dict[i]:
#         if not visited[path]:
#             added_visits.append(path)
#         visited[path] = True
#     if False not in visited:
#         max_pop = max(max_pop,pop)
#         # print(max_pop)
#         return
#     for j,v in enumerate(visited[1:]):
#         if not v:
#             dfs(j+1,pop+populations[j+1])
#     for path in added_visits:
#         visited[path] = False
#     return

# for i in range(1,N+1):
#     pop = populations[i]
#     visited[i] = True
#     added_visits = [i]
#     for path in path_dict[i]:
#         if not visited[path]:
#             added_visits.append(path)
#         visited[path] = True
#     dfs(i,pop)
#     for path in added_visits:
#         visited[path] = False

# print(max_pop)

# 2. DP,dfs
import collections
import sys

sys.setrecursionlimit(10**6)

N = int(input())
populations = [0]+list(map(int,input().split(' ')))
path_dict = collections.defaultdict(list)
for _ in range(N-1):
    town1,town2 = map(int,input().split(' '))
    path_dict[town1].append(town2)
    path_dict[town2].append(town1)

DP = [[populations[i],0] for i in range(N+1)]        # DP[N] = [a,b] : a = N번째 마을을 추가했을 때, b는 추가하지 않았을 때

visited = [True] + [False]*N

def dfs(cur):
    visited[cur] = True
    for town in path_dict[cur]:
        if not visited[town]:
            dfs(town)
            DP[cur][0] += DP[town][1]                   # 현재 노드를 추가할 경우 하위 노드를 추가하지 않은 경우를 더해줌
            DP[cur][1] += max(DP[town][0],DP[town][1])  # 현재 노드를 추가하지 않을 경우 하위 노드를 만족시킬 수 있는 경우의 최댓값을 더해줌

dfs(1)
print(max(DP[1]))