# 점프왕 쩰리 (Small)

from collections import deque
import sys
n = int(sys.stdin.readline())

area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 방문 유무 확인
visited = [[False]*n for _ in range(n)]               # [[False, False, False], [False, False, False], [False, False, False]]


# 이동할 방향 정의 (하,우)  상  하  좌 우
dx = [1, 0]             # [-1, 1,  0, 0]
dy = [0, 1]             # [0,  0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):

    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))

    # 큐가 빌 때 까지 반복
    while queue:
        x, y = queue.popleft()

        # 현재 밟고 있는 칸의 숫자 확인
        step = area[x][y]

        if area[x][y] == -1:
            return True

        # 현재 위치에서 두 방향(아래,오른쪽)으로 위치 확인
        for i in range(2):
            nx = x + dx[i]*step
            ny = y + dy[i]*step

            # 범위 안에 있고, 아직 방문하지 않았으면 방문 체크 후 queue에 넣기
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny))

# BFS를 수행한 결과 출력
if bfs(0,0):
    print('HaruHaru')
else:
    print("Hing")



