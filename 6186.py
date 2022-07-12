# Best Brass

import sys
R, C = map(int, sys.stdin.readline().split())

graph = []
for i in range(R):
    graph.append(list(sys.stdin.readline().strip()))  

count = 0
def dfs(x,y):
    global count 
    if x <= -1 or x >= R or y <= -1 or y >= C:
        return  False
    
    if graph[x][y] == '#':
        count += 1
        graph[x][y] = 0

        dfs(x-1, y)  # 좌
        dfs(x, y-1)  # 하
        dfs(x+1, y)  # 우
        dfs(x, y+1)  # 상
        return True
    return     # 종료

result = 0
for a in range(R):
    for b in range(C):
        # dfs 수행
        if dfs(a,b) == True:
            result += 1

print(result)
