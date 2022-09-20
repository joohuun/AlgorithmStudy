from collections import deque

'''
    N = 정점의 갯수
    M = 정점을 잇는 변의 갯수
    V = 시작 정점의 번호
'''

N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    

dfs_visited = [False] * (N+1)
bfs_visited = [False] * (N+1)

def dfs(V):
    dfs_visited[V] = True
    print(V, " ")
    for i in range(V, N+1):
        if not dfs_visited[i] and graph[V][i]:
            dfs(i)
            
def bfs(V):
    queue = deque([V])
    bfs_visited[V] = True
    while queue:
        V = queue.popleft()
        print(V, " ")
        for i in range(1, N+1):
            if not bfs_visited[i] and graph[V][i]:
                queue.append(i)
                bfs_visited[i] = True
        
bfs(V)
print()
dfs(V)
                
            