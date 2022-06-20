# 부당한 퍼즐

# 잘못된풀이 (문제이해 잘못함)
n = int(input())                    # 5
first = input().split(' ')          # ['1', '2', '3', '4', '5']
second = input().split(' ')         # ['4', '3', '2', '1', '5']
                                        
sequence = []

if second[::-1] == first:                                                        # 뒤집기만 했는데 같은 경우
    print("good puzzle")
elif second[::-1] != first:                                                      # 뒤집기 했을 때 같지 않는 경우 -> 밀기 해줘야함
    if sequence.append(second[n-1]) + sequence.append(second[0:n-1]) == first:   # (뒤집기 + 밀기 같은 경우) 
        print("good puzzle")
    else:                                                                        # (뒤집기 + 밀기 같지 않는 경우)
        print("bad puzzle")
elif sequence.append(second[n-1]) + sequence.append(second[0:n-1]) == first:     # 밀기만 했는데 같은 경우
    print("good puzzle")
elif sequence.append(second[n-1]) + sequence.append(second[0:n-1]) != first:     # 밀기 했을 때 같지 않은 경우 -> 뒤집기 해줘야함
    if second[::-1] == first:                                                    # (밀기 + 뒤집기 같은 경우)
        print("good puzzle")
    else:                                                                        # (밀기 + 뒤집기 같지 않는 경우)
        print("bad puzzle")

############ 동작은 몇 번이라도 수행할 수 있다 -> 이 문구 뒤늦게 발견


# 정답풀이
from collections import deque
import sys

N = int(sys.stdin.readline())       
sequence_1 = deque(sys.stdin.readline().split())                 # deque(['1', '2', '3', '4', '5'])
reversed_sequence_1 = deque(reversed(sequence_1))                # deque(['5', '4', '3', '2', '1'])
sequence_2 = deque(sys.stdin.readline().split())                 # deque(['4', '3', '2', '1', '5'])

for _ in range(N):
    if sequence_1 == sequence_2 or reversed_sequence_1 == sequence_2:
        print('good puzzle')
        break
    sequence_1.rotate(1)   # deque를 한칸씩 오른쪽으로 이동 
    reversed_sequence_1.rotate(1)
else:
    print('bad puzzle')


