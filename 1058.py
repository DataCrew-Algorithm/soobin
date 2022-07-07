# 친구
# 플로이드 와샬 + 그림설명

import sys

n = int(sys.stdin.readline())

graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().strip())) 

friend = [[0] * n for _ in range(n)]  

for k in range(n):                 # k = 거쳐갈 노드
    for i in range(n):             # i = 시작 노드
        for j in range(n):         # j = 도착 노드

            if i == j:             # 대각선 위치(자기자신 -> 자기자신)는 패스 
                continue

            if graph[i][j] == 'Y': # 시작 -> 도착 
                friend[i][j] = 1
                
            if graph[i][k] == 'Y' and graph[k][j] == 'Y': # 시작 -> 거치고 -> 도착
                friend[i][j] = 1

result = 0
for i in range(n):
    result = max(sum(friend[i]), result)
print(result)

# [[0, 1, 1, 0, 1, 0, 0, 0, 0, 1], 사람 1의 친구 4명 , 0 -> 4
#  [1, 0, 1, 0, 1, 0, 1, 1, 0, 1], 사람 2의 친구 6명 , 4 -> 6
#  [1, 1, 0, 1, 1, 1, 0, 0, 1, 1], 사람 3의 친구 7명 , 6 -> 7
#  [0, 0, 1, 0, 1, 1, 0, 0, 0, 0], 사람 4의 친구 3명 , 7 -> 7
#  [1, 1, 1, 1, 0, 1, 1, 1, 0, 1], 사람 5의 친구 8명 , 7 -> 8
#  [0, 0, 1, 1, 1, 0, 0, 0, 1, 0], 사람 6의 친구 4명 , 8 -> 8
#  [0, 1, 0, 0, 1, 0, 0, 1, 0, 0], 사람 7의 친구 3명 , 8 -> 8
#  [0, 1, 0, 0, 1, 0, 1, 0, 0, 0], 사람 8의 친구 3명 , 8 -> 8
#  [0, 0, 1, 0, 0, 1, 0, 0, 0, 0], 사람 9의 친구 2명 , 8 -> 8
#  [1, 1, 1, 0, 1, 0, 0, 0, 0, 0]] 사람 10의 친구 4명 , 8 -> 8
