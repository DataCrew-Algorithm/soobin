# 소수 구하기

# case1) (n-1)! = -1 (mod n) 이용
# 메모리초과 ..... 12부터 안됨 + 너무 느림 (비효율)
# import sys
# M, N = map(int, sys.stdin.readline().split()) # 3 6

# num = []
# for _ in range(M, N+1):
#     num.append(_)
# # print(num) [3, 4, 5, 6]

# cal = 1
# result1 = []
# result2 = []
# for i in num: # 3 4 5 6
#     for j in range(1, i, 1): # i=3일때 1부터 2까지 -> (n-1)!로 계산 해야되므로 
#         cal = cal * j
#         result1.append(cal)
#     result2.append(result1[-1])
#     cal = 1 # 초기화
# # print(result2) [2, 6, 24, 120]

# result_list = []
# for k in range(N-M+1): # M 부터 N 까지의 개수 : 3 4 5 -> 3개 (5-3+1)
#     for l in range(1,1000000):
#         result3 = result2[k] - num[k]*l
#         if result3 == -1:
#             print(num[k])
#     result_list = []

# case2) 에라토스테네스의 체
# https://blog.naver.com/cleveryellowduck/222803903347 참고 (404ms)
'''
범위에서 합성수를 지우는 방식
1. 1은 제거
2. 지워지지 않은 수 중 제일 작은 2를 소수로 채택
3. 나머지 2의 배수 모두 지움
4. 지워지지 않은 수 중 제일 작은 3을 소수로 채택
5. 나머지 3의 배수 모두 지움
6. 지워지지 않은 수 중 제일 작은 5를 소수로 채택
7. ... 반복
'''

import sys
M, N = map(int, sys.stdin.readline().split())
_list = [False, False] + [True] * (N-1)
#          0      1         2 3 4 5 ...
#       0과 1은 소수 아님    2부터는 일단 true라 하고 for문에서 해결하자

result = []
sqrt_n = int(N**0.5) # n의 최대 약수는 sqrt(n) 이하 -> sqrt_n까지만 검사
for i in range(2, sqrt_n+1):
    if _list[i]:
        for j in range(2*i, N+1, i): # 지워지지 않은 수 중 제일 작은 2를 소수로 채택, 나머지 2의 배수는 false로 변경
            _list[j] = False

for i in range(2, N+1):
    if _list[i] and i >= M:
        result.append(i)
for i in result:
    print(i)