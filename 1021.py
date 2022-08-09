# 회전하는 큐

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
target  = deque(map(int, sys.stdin.readline().split()))
queue = deque(range(1, N+1))

total_count = 0
while len(target) > 0:
    if target[0] == queue[0]:
        queue.popleft() # queue 첫번째 원소 뽑아내는 경우
        target.popleft() # 주어진 target도 뽑아버림

    elif queue.index(target[0]) <= len(queue)//2: 
        queue.rotate(-1) # 오른쪽으로 한 칸 이동
        total_count += 1

    else:
        queue.rotate(1) # 왼쪽으로 한 칸 이동
        total_count += 1

print(total_count)
